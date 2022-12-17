#BILHAR

from math import *

x, y = map(int, input().split())
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
def distance(x, a, y, b):
    return sqrt((a - x)**2 + (b -y)**2)
distancia1 = distance(x, a1, y, b1)
distancia2 = distance(x, a2, y, b2)
distancia3 = distance(x, a3, y, b3)
print(distancia1)
print(distancia2)
print(distancia3)
if distancia1 == min(distancia1, distancia2, distancia3):
    print(1)
elif distancia2 == min(distancia1, distancia2, distancia3):
    print(2)
else:
    print(3)