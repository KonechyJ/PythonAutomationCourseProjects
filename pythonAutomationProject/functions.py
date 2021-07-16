import random
import sys


def hello(name):
    print("Hello There")
    print("General " + name)

def randomIntGenerator():
    print(random.randint(1, 10))

def loop():
    for i in range (10):
        randomIntGenerator()

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)
hello("Kenobi")
loop()

#-------------------------------------------------------------------------------







