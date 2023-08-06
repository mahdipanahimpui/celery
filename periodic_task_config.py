from celery.schedules import crontab

beat_schedule = {
    'call_show_every_one_minute': {
        'task': 'periodic_tasks.print_name',
        'schedule': crontab(minute='*/1'), # every one minutes
        'args': ('mahdi',) # must be a tuple

    }
}


#### How Run ####

# after run worker for the main file: celery -A periodic_tasks worker -l info

# run beat too
# celery -A periodic_tasks beat
