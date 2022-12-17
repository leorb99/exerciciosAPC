#CALCULO DE PONTECIA V2
from math import pow
# NAO SEI O QUE ACONTECEU NOS TESTES OCULTOS (ERA A FORMATAÇAO .:1f, DEVERIA SER APENAS :)
x, y = map(int, input().split())
def powAPC(x, y):
    print(f'{pow(x, y):}') #assim o python decide quantas casas decimais usa tnc
powAPC(x, y)