# Saindo o Pedido

hamburguer = int(input())
batata = int(input())
refri = int(input())
milkshake = int(input())
salada = int(input())
pedido = {
    'hamburguer': hamburguer, 
    'batata': batata, 
    'refrigerante': refri, 
    'milkshake': milkshake, 
    'salada': salada
    }

for k in pedido:
    if pedido[k] > 0:
        print(f'Pedido com {pedido[k]} {k}(s)!')