# Palíndromo Mais Longo

s = input()
hist = {}
soma = 0
primeiroImpar = False
impar = False

for char in s:
    hist[char] = s.count(char)

for valor in sorted(hist.values()):    
    if valor % 2 == 0:
        soma += valor
    else:
        impar = True
        soma += (valor - 1)
if impar == True:
    print(soma+1)
else:
    print(soma)

# versao enviada no moodle
for valor in sorted(hist.values()):    
    if valor % 2 and primeiroImpar == True:
        soma += (valor-1)
    elif primeiroImpar == False and valor % 2:
        primeiroImpar = True
        soma += valor
    else:
        soma += valor
        
print(soma)
