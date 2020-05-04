from django.utils import timezone
from celery.schedules import crontab
from celery.task import periodic_task

from .models import GatheringSpot


@periodic_task(run_every=crontab(minute='*/1'))
def delete_old_reports():
    reports = GatheringSpot.objects.all()
    print(reports)
    for report in reports:
        if report.expiration_date < timezone.now():
            report.delete()
