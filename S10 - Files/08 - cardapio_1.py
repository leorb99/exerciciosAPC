# Cardapio 1

pedido = input()
nao_tem = False

with open('cardapio.txt', 'r') as arquivo:
    valor = 0
    for linha in arquivo:
        prato = linha.strip('\n')
        prato = prato.split('/')
        if pedido in prato[0] or pedido.capitalize() in prato[0]:
            print(f'{prato[0]}')
            nao_tem = True
        
if nao_tem == False:     
    print('Infelizmente não temos este prato')


# Pão de queijo/8.00
# Feijoada/30.00
# Feijoada vegana/25.90
# Arroz com feijão/15.00
# Farofa de ovo/9.90
# Farofa de banana/9.90
# Moqueca capixaba/40.00
# Carne de sol/35.00
# Filé/25.00
# Filé de frango/21.90
# Risoto de carne/25.00
# Risoto de camarão/30.00
# Risoto de cogumelo/25.00
# Risoto de frango/21.00
# Nhoque/20.90
# Lasanha de presunto/30.00
# Lasanha de frango/30.00
# Espaguete/25.00
# Ravioli/30.00
# Panqueca de carne/25.00
# Panqueca de frango/22.90
# Acarajé/12.00
# Tapioca de carne de sol/10.00
# Tapioca de queijo/8.90
# Tapioca de manteiga/6.90
# Pato no tucupi/40.00
# Tacacá/25.90
# Açaí/10.90
# Churrasco/45.90
# Churrasco de melancia/29.90
# Tainha/20.90
# Barreado/18.90
# Arroz com pequi/15.00
# Pintado à urucum/20.90
# Caldo de piranha/18.90
# Pizza de muçarela/25.00
# Pizza de marguerita/30.00
# Pizza de calabresa/30.00
# Pizza de pepperoni/35.90
# Hambúrguer/30.00
# Pizza de banana/30.00
# Pudim de leite/7.00
# Bolo de cenoura/6.00
# Brigadeiro/5.00
# Cocada/5.00