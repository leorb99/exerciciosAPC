#TRIANGULO RECURSIVO V2
def triangulo(x, size):
    if size >= 1 and x != 0:
        print(' ' * (x - 1), '*' * size)
        triangulo(x + 1, size - 2)
    elif size >= 1 and x == 0:
        print('*' * size)
        triangulo(x + 1, size - 2)

triangulo(0, 5) #numero de linhas do triangulo = size // 2 + 1
triangulo(3, 7)
triangulo(6, 9)
triangulo(6, 9)   