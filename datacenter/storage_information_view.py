from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.models import get_duration
from datacenter.models import is_visit_long
from datacenter.models import format_duration
  

def storage_information_view(request):
    non_closed_visits = []

    visits_nonclosed=Visit.objects.filter(leaved_at__isnull = True)

    for in_bank in visits_nonclosed:
        passcard = in_bank.passcard
      
        non_closed_visits.append({
                'who_entered': passcard.owner_name, 
                'entered_at':timezone.localtime(in_bank.entered_at), 
                'duration': format_duration(in_bank)
        })

    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
