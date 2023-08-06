from celery import Celery
from person import Person

# serializer: a way to send data like
# json, pickle, YAML, 

# note: json not supported complex type like objects


# by default:

############             ##########            ############
# producer #  >> json >> # broker # >> json >> # consumer #
############             ##########            ############








app = Celery('serializer', broker="amqp://guest:guest@localhost:5672", backend='rpc://')

app.conf.update(
    task_serializer = 'pickle', # the data type that publisher produce
    result_serializer = 'pickle', # returned result type format
    accept_content =  ['application/x-python-serialize'] # witch type of data is allowed to get in celery 
)


p = Person('mahdi')

@app.task
def call(person):
    return person.show()




# in terminal:
# create object in terminal, 
# to use ind code: comment and decomment after run worker

result = call.delay(p)
print(result.get())





