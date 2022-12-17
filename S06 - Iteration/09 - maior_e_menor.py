#Maior e menor

# array = [n] * 5

n = int(input())
menor = 100000
maior = 0
while n > 0:
    x = int(input())
    n -= 1
    if menor > x:
        menor = x
    if maior < x:
        maior = x
        if menor > 0:
            x = menor
print('Menor:', menor)
print('Maior:', maior)