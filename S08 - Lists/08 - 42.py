# 42

n = int(input())
lista = list(map(int, input().split()))
soma = 0
lista.sort()

for i in range(len(lista)-1):
    for j in range(1, len(lista)):
        if i == j:
            continue
        if soma == 42:
            break
        soma = lista[i] + lista[j]

if soma == 42:
    print('sim')
elif soma != 42:
    print('nao')



# MAIS EFICIENTE 
# T = int(input())
# # lista = [22,10,42,5,20,12,13,15,94,100]
# lista = [1,2,2,42,2]
# # lista = [61,12,25,8,88,25,90,69,90,13,62,7,84,40,54,27,2,50]

# verify = []

# def funct(T: int, lista: list, verify: list):
#     for i in lista:
#         soma = T - i
#         if soma not in verify:
#             verify.append(i)
#         elif soma in verify:
#             return "sim"
#     return "nao"

# print(funct(T, lista, verify))