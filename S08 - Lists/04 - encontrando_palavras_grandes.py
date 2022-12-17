# Encontrando Palavras Grandes

lista = input().split()
print(lista)
for i in lista:
    if len(i) > 6:
        print(i)