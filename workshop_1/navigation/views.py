from datetime import datetime, timedelta
import django.utils.timezone as tz
from django.db.models import F
from django.http import JsonResponse
from .models import *


def latest(request):

    latest_pos = NavigationRecord.objects.filter(
        datetime__range=[datetime.now() - timedelta(days=2), datetime.now()]) \
        .order_by('vehicle', '-datetime').distinct('vehicle') \
        .annotate(plate=F('vehicle__plate')).values()

    
    points = [{
        'latitude': row.get('latitude'), 'longitude': row.get('longitude'), 'plate': row.get('plate'),
        'datetime': tz.datetime.strftime(row.get('datetime'), "%d.%m.%Y %H:%M:%S")
    } for row in latest_pos]

    return JsonResponse(data=points, safe=False, json_dumps_params={'indent': 1})


