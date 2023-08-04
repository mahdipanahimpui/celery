from celery import Celery
import time

# <backend> is used to save the result of task, (rpc > is rabbitmq),
# it is possibel to save result in a database like redis 
app = Celery('two', broker="amqp://root:000@localhost:5672", backend='rpc://')


@app.task(name='three.add')
def add(a, b):
    time.sleep(30)
    return a / b

    

# in terminal ::

# r = add.dealy(4,2)
# r.ready() # True or False
# r.get() # get the value, block the app until response is returned
# r.get(timeout=10) # if result is not prepared wait for 10 seconds 

# if on running a task, an error raised, the error is returned to app in <get>, 
# to prevent set propagate=False, returned an string error insted error
# r.get(propagate=False)

# state: returns the status of task in terminal
# r.status   note: after r.get() status changes to SUCCESS, not after doing task