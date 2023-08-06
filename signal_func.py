from celery import signals

@signals.task_prerun.connect() # to limit a specific task, (sender=add)
def show(sender=None, **kwargs):
    print('task befor run')
    print(sender)
    print(kwargs)