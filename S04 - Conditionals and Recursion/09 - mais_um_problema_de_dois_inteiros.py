#MAIS UM PROBLEMA DE DOIS INTEIROS
from math import *
def jogadas(a, b):
    if a > b:
        print(ceil((a - b) / 10))
    else:
        print(ceil((b - a) / 10))

jogadas(5, 5) #0
jogadas(13, 42) #3
jogadas(18, 4) #2
jogadas(1337, 420) #92
jogadas(1234, 10000) #877
jogadas(100500, 9000) #9150