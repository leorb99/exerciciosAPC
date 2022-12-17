# Estatísticas I
from math import sqrt

X = list(map(int, input().split()))
media = sum(X) / len(X)
desvio = []
# for i in X:
#     if i > media:
#         desvio.append(((i-media)**2))
#     else:
#         desvio.append(((media-i)**2))
#     variancia = sum(desvio) / len(X)
# print(f'{variancia:.1f}\n{sqrt(variancia):.1f}')

# usando compreensao de listas
desvio = [(i - media) ** 2 for i in X if i > media]
desvio = [(media - i) ** 2 for i in X]
variancia = sum(desvio) / len(X)
print(f'{variancia:.1f}\n{sqrt(variancia):.1f}')

