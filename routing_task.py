from celery import Celery, signals


app = Celery('routing_task', broker="amqp://guest:guest@localhost:5672")
app.config_from_object('queue_config')

@app.task()
def add(a,b):
    return a + b


@app.task()
def sub(a,b):
    return a - b

@app.task()
def div(a,b):
    return a / b


@signals.task_postrun.connect
def show_task_info(sender=None, **kwargs):
    print(sender.request)