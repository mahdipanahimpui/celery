# from celery import Celery, signals


# app = Celery('routing_task', broker="amqp://guest:guest@localhost:5672")
# app.config_from_object('queue_config')

# @app.task()
# def add(a,b):
#     return a + b


# @app.task()
# def sub(a,b):
#     return a - b

# @app.task()
# def div(a,b):
#     return a / b


# @signals.task_postrun.connect
# def show_task_info(sender=None, **kwargs):
#     print(sender.request)

from celery import Celery, signals
from kombu import Exchange, Queue

app = Celery('your_app_name', broker='amqp://guest:guest@localhost:5672')

# Configure the worker pools for different task queues
app.conf.task_queues = (
    Queue('fork_queue', 
          Exchange('fork_exchange'), 
          routing_key='fork_queue'),
    Queue('eventlet_queue', 
          Exchange('eventlet_exchange'), 
          routing_key='eventlet_queue'),
)

# it is not requeired to declare pool and concurrency here
# it is required to declare in terminal when you want to start a worker
app.conf.task_annotations = {
    'concurrency.fork_task': {'pool': 'fork', 'concurrency': 4},
    'concurrency.eventlet_task': {'pool': 'eventlet', 'concurrency': 8}
}

@app.task(queue='fork_queue', )
def fork_task(arg):
    # Task logic using 'fork' pool
    print('fork_task')

@app.task(queue='eventlet_queue')
def eventlet_task(arg):
    # Task logic using 'eventlet' pool
    print(eventlet_task)


@signals.task_postrun.connect
def show_task_info(sender=None, **kwargs):
    print(sender.request)


# celery -A concurrency worker -l info -Q fork_queue --pool=prefork --concurrency=7 
# pip install eventlet
# celery -A concurrency worker -l info -Q eventlet_queue --pool=evenlet --concurrency=70


# note:
# by default concurrency is 4 (i think)
# by default pool type is fork

# fork => cpu bound
# eventlet => I/O bound
# solo => (used for huge computation, use whole CPU) means concurency=1, evern the concurrency is not 1,
# note: it is good >> --pool=solo --concurrency=1 << set the concurrency to 1








