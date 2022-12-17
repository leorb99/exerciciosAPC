#PISCINA DA MANSAO
'''a, b, c = map(int, input().split())
def print_rectangle(var):
    print(f'{var}')
    print('+' * var)
    print('+' + ' ' * (var - 2) + '+')
    print('+' * var)
print_rectangle(a)
print_rectangle(b)
print_rectangle(c)
TAVA ARRUMANDO O CODIGO ANTES DO MONITOR FALAR SOBRE CHAMAR A FUNCAO 3 VEZES
NAO TINHA PASSADO EM ALGUM TESTE OCULTO
'''

a, b, c = map(int, input().split())
def print_rectangle(var):
    print(f'{var}' + '\n' + '+' * var + '\n' + '+' + ' ' * (var - 2) + '+' + '\n' + '+' * var)
print_rectangle(a)
print_rectangle(b)
print_rectangle(c)