#DIVIDINDO DOCES
n = int(input())
m = int(input())
docesRecebidos = n / (m + 1)
restoDosDoces = n - (int(docesRecebidos) * (m + 1))
print(int(docesRecebidos))
print(int(restoDosDoces))