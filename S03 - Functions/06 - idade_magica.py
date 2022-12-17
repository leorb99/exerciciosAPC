#IDADE MAGICA
a, b, c = map(int, input().split())
'''
def calcular(var):  # o nome deveria ser converte ne, agr ja foi
    ano = var // 360 # converte a variavel em ano(s)
    mes = (var // 30) % 12 # converte a variavel em mes(es)
    dia = var % 30 # converte a variavel em dia(s)
    print(f'{ano} ano(s), {mes} mes(es) e {dia} dia(s)') #podia ter colocado o calculo dentro das chaves
def age(a, b, c):
    calcular(a)
    calcular(b)
    calcular(c)
age(a, b, c)
'''
'''

def age(a, b, c):
    print(f'{a // 360} ano(s), {(a // 30) % 12} mes(es) e {a % 30} dia(s)')
    print(f'{b // 360} ano(s), {(b // 30) % 12} mes(es) e {b % 30} dia(s)')
    print(f'{c // 360} ano(s), {(c // 30) % 12} mes(es) e {c % 30} dia(s)')
age(a, b, c)
'''

def age(var):
    print(f'{var // 360} ano(s), {(var // 30) % 12} mes(es) e {var % 30} dia(s)')
age(a)
age(b)
age(c)