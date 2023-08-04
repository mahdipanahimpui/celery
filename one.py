from celery import Celery

app = Celery('one', broker="amqp://root:000@localhost:5672")

# use this command to start
# celery -A one worker -l info