from datetime import timedelta, datetime
from geojson import Point
from django.shortcuts import redirect
from django.utils import timezone

from .models import GatheringSpot


# Create your views here.
def submit_report(request):
    g = GatheringSpot(
        number=int(request.GET.get('number')),
        action=request.GET.get('action'),
        geom=Point((float(request.GET.get('lng')), float(request.GET.get('lat')))),
        expiration_date=timezone.now() + timezone.timedelta(seconds=15)
    )
    g.save()
    return redirect("/")
