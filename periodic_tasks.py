from celery import Celery


app = Celery('periodic_tasks', broker="amqp://guest:guest@localhost:5672")
app.config_from_object('periodic_task_config')

@app.task()
def print_name(name):
    print(name)
