# Escolha Premiada

# uma lista e um int(n) entram, se for possivel somar os numeros da lista
#e o resultado for = n eh possivel ganhar se nao eh impossivel

# [1, 2, 3, 8] n = 10 2 + 8 = 10 -> eh possivel ganhar
# [1, 2, 3, 8] n = 7 nenhuma combinacao dos numeros da lista eh igual a n -> impossivel
from itertools import combinations

v = list(map(int, input().split()))
n = int(input())
soma = 0
possivel = False

for i in range(len(v)):
    for soma in combinations(v, i):
        soma = sum(soma)
        if soma == n:
            possivel = True
            break

if possivel == True:
    print('E possivel ganhar.')
else:
    print('Impossivel ganhar.')
