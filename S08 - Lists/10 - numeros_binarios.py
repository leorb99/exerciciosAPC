# Números binários

# M, N = map(int, input().split())
# X1 = list(map(int, input().split()))
# X2 = list(map(int, input().split()))
# final = []

# # converte o numero binario em decimal para facilitar o calculo
# def conversor(digitos, tamBinario):   
#     decimal = 0
#     j = 1
#     for i in digitos:                        
#         while j <= tamBinario:
#             decimal += (i * 2**(-j))
#             j += 1
#             break
#     return decimal

# soma = conversor(X1, M) + conversor(X2, N)
# if soma >= 1:
#     soma -= 1

# while True:
#     soma *= 2
#     final.append(int(soma))
#     if soma > 1:
#         soma -= 1
#         break
# for i in final:
#     print(f'{i}', end=' ')

M, N = map(int, input().split())
X1 = list(map(int, input().split()))
X2 = list(map(int, input().split()))
sobeUm = False
result = []
n = -1

while len(X1) > len(X2):
    X2.append(0)
while len(X2) > len(X1):
    X1.append(0)

for i, j in zip(X1[::-1], X2[::-1]):
    if (i + j == 2 and sobeUm == False) or (i + j == 1 and sobeUm == True):
        result.insert(n, 0)
        sobeUm = True
    elif i + j == 2 and sobeUm == True:
        result.insert(n, 1)
        sobeUm = True
    elif i + j == 1 and sobeUm == False:
        result.insert(n, 1)
    elif i + j == 0 and sobeUm == True:
        result.insert(n, 1)
        sobeUm = False
    elif i + j == 0 and sobeUm == False:
        result.insert(n, 0)
    n -= 1

if len(result) > 1:   
    while result[-1] == 0:
        result.pop()
print(*result)

# 3 5
# 0 0 1
# 1 1 0 0 1
# 1 1 1 0 1

# 6 6
# 1 0 1 0 0 1
# 1 1 0 0 1 1
# 0 1 1 1

# 5 4
# 1 0 1 1 1
# 0 0 0 1
# 1 1 0 0 1

# 6 2
# 1 1 0 1 1 1
# 1 1
# 1 0 0 1 1 1

# 1 1
# 0
# 0
# 0

# 9 4
# 1 0 1 0 1 1 0 0 1
# 1 1 0 1
# 0 1 1 1 1 1 0 0 1	

# 1 1 
# 1
# 1
# 0
