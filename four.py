from celery import Celery
import time

## 3 way to set config

app = Celery('one', broker="amqp://root:000@localhost:5672", backend='rpc://')

# way1:
# app.config.result_backend = 'rpc://'

# way2: (using other file)
# app.config_from_object('celery_conf')


# way3:
app.conf.update(
    task_time_limit = 60, # limit of time that a worker can work on a task, after that kill the task, r.get() raise error after time limit
    task_soft_time_limit = 50, # after this time raise an exception, and not kill suddenly

    #If you’re doing mostly I/O you can have more processes, but if mostly CPU-bound, 
    # try to keep it close to the number of CPUs on your machine. 
    # If not set, the number of CPUs/cores on the host will be used.
    worker_concurrency = 4, # 5 cpu in my sys is active, 1 is reserved

    worker_prefetch_multiplier = 1, # how devide tasks between worker, default is 4, 0 is charge of celery
    task_ignore_result = False, # it is False by default, if True worker, work better, but not returns results. can use in task(seel below)
    task_always_eager = False, # it is False by default, task run in the client sys, used in debug or test, (in get block the app until respose get)
    task_acks_late = True, # celery check(تیک زدن) the task when got not when done, to prevent this task_acks_late = True,
)





@app.task(name='one.add' """ all of above could use specially here """) 
def add(a, b):
    time.sleep(20)
    return a + b