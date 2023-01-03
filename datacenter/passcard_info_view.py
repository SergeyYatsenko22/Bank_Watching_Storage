from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.models import get_duration
from django.shortcuts import get_object_or_404
from datacenter.models import is_visit_long
from datacenter.models import format_duration


def passcard_info_view(request, passcode):
    this_passcard = get_object_or_404(Passcard, passcode=passcode)
    this_visits = Visit.objects.filter(passcard__passcode=passcode,
                                        leaved_at__isnull=False)
    this_passcard_visits = []

    for visit in this_visits:
        
        this_passcard_visits.append({
            'entered_at': timezone.localtime(visit.entered_at), 
            'duration': format_duration(visit), 
            'is_strange': is_visit_long (visit)
        })
                 
    context = {
        'passcard': this_passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
