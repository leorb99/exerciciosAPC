# Cardapio 2

pedido = input()
nao_tem = False

with open('cardapio.txt', 'r') as arquivo:
    valor = 0
    for linha in arquivo:
        prato = linha.strip('\n')
        prato = prato.split('/')
        if pedido in prato[0] or pedido.capitalize() in prato[0]:
            valor += float(prato[1])
            print(f'{prato[0]} {prato[1]}')
            nao_tem = True
        
if nao_tem == True:
    print(f'Sua conta deu: {valor:.2f}')
elif nao_tem == False:     
    print('Infelizmente não temos este prato')