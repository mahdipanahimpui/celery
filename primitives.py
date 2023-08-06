from celery import Celery, chain, group
import time


##### Primitives #####

# rpc needs in get result in code
app = Celery('primitives', broker="amqp://guest:guest@localhost:5672", backend='rpc://')


@app.task(name='primitives.add')
def add(a, b):
    time.sleep(1)
    return a + b

@app.task(name='primitives.sub')
def sub(a,b):
    return a - b



### Chains
# work like pipe line, the result of previous is the first agr of the next 
# my_chain = chain(add.signature((1,2)), sub.signature((3,)))
# # print(my_chain)

# print('result: ',my_chain().get()) # used to see result of chain
# print('parent result: ', my_chain().parent.get()) # could use many parents



### Group
# run many task async, together
# my_group = group(add.signature((1,2)), sub.signature((4,5)))
# print(my_group().get())


# other Example
# jobs = group([
#     add.signature((10,20)),
#     sub.signature((100,200))
# ])

# results = jobs.apply_async()
# print(results.ready())
# time.sleep(15)
# print(results.completed_count()) # befor results.get() completed count is 0 (this is an issue)
# print(results.get()) # just after get(), ready() returns True
# print(results.ready())



### Chords
# not available in rpc,
# if all task runs ok in chords, and callback will be run at the end


### Chunks
# let you to run a batch of task part by part

result = add.chunks(zip(range(20), range(20,40)), 5)
print(result().get())