#Co-primos

a, b = map(int, input().split())

def mdc(a, b):
    while b > 0:
        aux = a % b
        a = b
        b = aux
    return a

if mdc(a, b) == 1:
    print('Sao co-primos.')
else:
    print('Nao sao co-primos!')