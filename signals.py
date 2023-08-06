from celery import Celery
import signal_func
import time

##### Signals #####


app = Celery('signals', broker="amqp://guest:guest@localhost:5672", backend='rpc://')


@app.task(name='signals.add')
def add(a, b):
    time.sleep(1)
    return a + b

@app.task(name='signals.sub')
def sub(a,b):
    return a - b


