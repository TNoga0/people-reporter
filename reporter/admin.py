from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from . import models

admin.site.register(models.GatheringSpot, LeafletGeoAdmin)