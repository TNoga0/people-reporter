from geojson import Point
from django.shortcuts import redirect

from .models import GatheringSpot


# Create your views here.
def submit_report(request):
    g = GatheringSpot(
        number=int(request.GET.get('number')),
        action=request.GET.get('action'),
        geom=Point((float(request.GET.get('lng')), float(request.GET.get('lat'))))
    )
    g.save()
    return redirect("/")
