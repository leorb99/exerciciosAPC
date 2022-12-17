#PEDRA, PAPEL, ATAQUE AEREO

#1 = Pedra
#2 = Papel
#3 = Ataque Aereo
def ppa(a, b):
    if (a == 3 and b < 3) or (a == 1 and b == 2):
        return 'Jogador 1 venceu'
    elif (b == 3 and a < 3) or (b == 1 and a == 2):
        return 'Jogador 2 venceu'
    elif a == 1 and b == 1:
        return 'Sem ganhador'
    elif a == 3 and b == a:
        return 'Aniquilacao mutua'
    else:
        return 'Ambos venceram' 
print(ppa(1, 1))
print(ppa(1, 2))
print(ppa(1, 3))
print(ppa(2, 2))
print(ppa(3, 3))
