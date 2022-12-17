# Lista de elementos

# def remove_duplicatas(lista):
#     return sorted(set(lista))   # forma roubada

def remove_duplicatas(lista):
    novaLista = []
    for i in lista:
        if i not in novaLista:
            novaLista.insert(i)
    return novaLista


print(remove_duplicatas([1,2,2,3]))
print(remove_duplicatas([1,1,1]))
print(remove_duplicatas([0,0,1,1,2,2,3,3]))
print(remove_duplicatas([0,0,1,1,2,2,3,4,4,5,5,5,5,5,6,6,6,6,7]))
print(remove_duplicatas([1,1,2,5,4,2,3,2]))