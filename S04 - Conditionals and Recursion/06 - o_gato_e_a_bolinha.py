#O GATO E A BOLINHA
from math import *
k = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
D = sqrt(pow(x2 - x1, 2) + pow(y2 -y1, 2))
if D == k:
    print('pfff... ta bom')
elif D > k:
    print('ta achando que eu sou cachorro?')
else:
    print('*miau* ta bom, vou buscar')