# celery has a one queue called celery

# task_default_queue = 'mahdi_sys' # default que if the specific queue for every task not defined

# task_routes = {
#     'routing_task.add': {'queue': 'first'},
#     'routing_task.sub': {'queue': 'second'}
# }


# to define the queue that is in task_routes run
# celery -A routing_task worker -l info -Q first,second



##### for more control use kombu #####

from kombu import Queue, Exchange

default_exchange = Exchange('default', type='direct')
media_exchange = Exchange('media', type='direct')

task_queues = ( # task_queues must be the name
    Queue('default', default_exchange, routing_key='default'),
    Queue('video', media_exchange, routing_key='video'),
    Queue('image', media_exchange, routing_key='image') # in direct Queue name == routing_key
)

# set the defaults:

task_default_queue = 'default' # name of queue
task_default_exchange = 'default' # name of exchange
task_default_routing_key = 'default' # name of routing_key


# how connect queues to tasks in 2 way

# 1>>
# in terminal:
# from routing_task import add 
# add.apply_async((4, 10), Queue='image') # give the queue name


# 2>>
task_routes = { # task_routes as the same name
    'routing_task.add': {'queue':'video'},
    'routing_task.sub': {'queue':'image'}
}

# by using kombu no nedd declare queue name in:
# celery -A routing_tak worker -l info 




