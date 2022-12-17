# Gabriel - maior e menor valores

lista = input().split()
lista = list(map(int, lista))
print(min(lista), lista.index(min(lista)))
print(max(lista), lista.index(max(lista)))
for i in lista:
    print(i, end=' ')