from celery import Celery
import time
# print is not prefered, logging is better
from celery.utils.log import get_task_logger 

app = Celery('two', broker="amqp://root:000@localhost:5672")
logger = get_task_logger(__name__)


# NOTE @app decorator should be the toppest decorator
# access to task in code by usign bind=True and sending self to def, 
@app.task(bind=True, name='two.add', default_retry_delay=600)
def add(self, a, b):
    # print(self.request) # to access the task
    try:
        return a / b
    except ZeroDivisionError:
        # print('sorry...') # loggin is better
        logger.info('sorry')

        # for this specific retry cutdown is prefered than default_retry_delay
        self.retry(countdown=10, max_retries=2) # by default retry is after 180s, default of max_retries is 3 times

    