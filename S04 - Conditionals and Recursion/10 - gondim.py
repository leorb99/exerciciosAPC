#GONDIM
from math import *
def classificador(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        print('triangulo')
        if a != b and a != c and b != c:
            print('escaleno')
        if a == b or a == c or b == c:
            print('isosceles')
        if a == b and a == c:
            print('equilatero')
        if pow(a, 2) == pow(b, 2) + pow(c, 2) or pow(b, 2) == pow(a, 2) + pow(c, 2) or pow(c, 2) == pow(b, 2) + pow(a, 2):
            print('retangulo')
    else:
        print('gondim sendo gondim')
classificador(3, 5, 4)
print()
classificador(2, 1, 1) 
print()
classificador(3, 3, 3)