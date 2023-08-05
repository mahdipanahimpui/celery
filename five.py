from celery import Celery
import time

### Signatures senario ###
## wraps the arguments, keyword arguments, 
# and execution options of a single task invocation in a way
# such that it can be passed to functions or even serialized and
# sent across the wire.
# packs the task to run task in other place, 

# in Signature Celery app name shuld be as same as module name
app = Celery('five', broker="amqp://root:000@localhost:5672", backend='rpc://')


@app.task(name='five.add')
def add(a, b):
    time.sleep(5)
    return a + b




my_task = add.signature((4,5), countdown=10) # use s insted signature
# print(my_task) # three.add(4, 5)
# print(my_task.options) # {'countdown': 10}


## How Run ##
my_task.delay() # no need args, because sent before




###<<< 3 feature is Signature >>>###

# 1: Partials #

partial = add.signature((5,)) # second arg not sent
# partial.delay(2) # or use apply_async
partial.apply_async((10,)) # completing signature by adding second arg

# it is possible to send all args where signatue want to run





# 2: callbacks

# used to sending result of a task to other task
# use apply_async

@app.task
def sub(a,b):
    return a - b

# link do as a callback
add.apply_async((4, 10), link=sub.signature((30,))) # second task is sub,(first add then sub)




# 3: immutability
# ignore the result of first task for second task, (avoid the callback)
# used when you want to run second task if the first is done ok
add.apply_async((4, 10), link=sub.signature((30,10)), immutable=True)











