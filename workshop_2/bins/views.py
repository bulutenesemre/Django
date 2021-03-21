from datetime import datetime, timedelta
import django.utils.timezone as tz
from django.db.models import F
from django.http import JsonResponse
from .models import *


def bin_operations(request):
    bin_values = BinOperation.objects.all() \
        .annotate(operation_name=F('operation__name'),
                  latitude=F('bin__latitude'),
                  longitude=F('bin__longitude'),
                  ).values()
    results = [{
        'operation_name': row.get('operation_name'),
        'frequency': row.get('operation_frequency'),
        'latitude': row.get('latitude'),
        'longitude': row.get('longitude'),
    } for row in bin_values]

    return JsonResponse(data=results, safe=False, json_dumps_params={'indent': 1})

