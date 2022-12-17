# Telefone novo

celular = {}
menor = 40000                                 # os precos lidos serao menores que 40k
repetido = []                                 # lista para guardar valores repetidos

for i in range(4):                            # laco para ler e formar o dict 
    nome = input()
    modelo = input()
    preco = int(input())
    for v in celular.values():                # olha apenas para os valores no dict
        if modelo == v[0]:                    # se o valor ja estiver no dict
            repetido.append(modelo)           # ele vai para a lista repetido
    celular[nome] = modelo, preco             # adiciona o modelo e o preco no dict

if len(repetido) == 0 or len(repetido) == 2:  # se a lista tiver 0 ou 2 valores
    for k in celular:                         # a pessoa escolhera o celular novo
        if celular[k][1] < menor:             # baseado no preco
            menor = celular[k][1]
            modelo = celular[k][0]
    print(modelo)
else:                                         # imprime o primeiro valor na lista repetido
    print(repetido[0])
