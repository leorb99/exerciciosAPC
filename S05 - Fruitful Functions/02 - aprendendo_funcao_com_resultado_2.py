#APRENDENDO FUNCAO COM RESULTADO 2

a = int(input())
b = int(input())
def subQuadrado(a, b):
    if a <= b:
        return (a - b)**2
    return a - b
print(subQuadrado(a, b))