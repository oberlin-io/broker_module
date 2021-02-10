import broker
import atexit


B = broker.Broker()


import random

def func1():
    return random.randint(0,9)

def func2(integer):
    return integer * 10

def func3(integer):
    return integer * 100



for i in range(3):
    B.publish('Random int', func1())

for message in B.queue:
    print(message)
print('- - -')


for payload in B.consume('Random int', 'func2'):
    B.publish('Random int * 10', func2(payload))

for message in B.queue:
    print(message)
print('- - -')


for payload in B.consume('Random int', 'func3'):
    B.publish('Random int * 100', func3(payload))

for message in B.queue:
    print(message)
print('- - -')


B.queue_to_disk()

atexit.register(B.queue_to_disk)
