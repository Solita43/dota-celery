import zoneinfo
from celery import shared_task
from django.core.cache import cache
from django_celery_beat.models import CrontabSchedule

@shared_task
def refresh_top_players_data():
    top_players_data = {"124234234": {
        "hero_id": 1,
    }}
    cache.set('top_players_data', top_players_data, 60 * 60 * 24)  # Cache the data for 24 hours

schedule, _ = CrontabSchedule.objects.get_or_create(
     minute='30',
     hour='*',
     day_of_week='*',
     day_of_month='*',
     month_of_year='*',
     timezone=zoneinfo.ZoneInfo('Canada/Pacific')
)
