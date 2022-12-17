# Bolão

n = int(input())
numSorteados = list(map(int, input().split()))
participantes = {}
ganhou = False

for i in range(n):
    dados = list(input().split('-'))
    participantes[dados[0]] = list(map(int, dados[1].split()))

for v in participantes:
    if participantes[v] == numSorteados:
        print('deu bom!', v, sep='\n')
        ganhou = True
        break
if ganhou == False:
    print('não foi dessa vez /:')