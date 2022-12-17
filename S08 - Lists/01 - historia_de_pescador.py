# Historia de Pescador

peixe = ''
rede = []
while peixe != 'acabou':
    peixe = input()
    rede.insert(peixe)
del rede[-1:]
print('Hoje eu pesquei:')
for i in rede:
    print(i)
