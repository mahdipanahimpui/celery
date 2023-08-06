from celery import Celery
import time

app = Celery('one', broker="amqp://guest:guest@localhost:5672")

# use this command to start
# celery -A one worker -l info



# to use celery syncronously
# name is optinal,
# recommends: unique name, use module name befor name
@app.task(name='one.add')
def add(a, b):
    time.sleep(10)
    return a + b

### how use celey asyncronously with <delay> and <apply_async>
## delay and apply_async are same apply_async is more optional


#### ex: task.delay(arg1, arg2, kwarg1='x', kwarg2='y')
#### ex: task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})

# EX 
# after run worker
# from celery import add
# add.delay(2, 3)
 

## << options >> ##
# cutdown
# after countdown seconds start to starting task, is not accurate
# add.apply_async(args=[2, 3], countdow=3)

# eta
# ETA(estimated time of arrival) gives a datetime, like cutdown

# from datetime import datetime, timedelta
# tomorrow = datetime.utcnow() + timedelta(days=1)
# add.apply_async((2, 2), eta=tomorrow)


# expires: 
# a int num as second or a date time, 
# << expire time is the time to start the tast not the end of response >> #
# celery ignore the tast
# add.apply_async(args=[5,5], expires=2, countdown=3)

