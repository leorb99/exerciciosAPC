# Converte de um sistema numerico (dividendo) para um sistema numerico (divisor)
# O resto de baixo pra cima eh o numero correspondente no novo sistema
dividendo, divisor = map(int, input('Digite o dividendo e o divisor: ').split())
def conversor(dividendo, divisor):
    var = dividendo
    if var > divisor:
        var = dividendo // divisor
        print(f'{dividendo} / {divisor} = {var}', 'resto:', (dividendo % divisor))
        conversor(var, divisor)
        if var == divisor:
            print(f'{var} / {divisor} = {var // divisor} resto:', var % divisor)
            print(f'{var // divisor} / {divisor} = 0 resto:', var // divisor)
    elif var < divisor:
        print(f'{var} / {divisor} = 0 resto:', var)
conversor(dividendo, divisor)