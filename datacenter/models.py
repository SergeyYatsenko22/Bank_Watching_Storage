from django.db import models
from django.utils import timezone


def get_duration(visit):
    time_in = timezone.localtime(visit.entered_at)
    time_out = timezone.localtime(visit.leaved_at)
    duration = (time_out - time_in).total_seconds()
    return duration


def format_duration(visit):
    hours_in_bank = int(get_duration(visit) // 3600)
    minutes_in_bank = int(get_duration(visit) % 3600 // 60)
    time_in_bank = (str(f"{hours_in_bank:02}"), ":",                                   
                    str(f"{minutes_in_bank:02}"))
    return ("".join(time_in_bank))


def is_visit_long(visit, minutes=60):
    return (get_duration(visit) / 60) >= minutes
  

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    
    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
