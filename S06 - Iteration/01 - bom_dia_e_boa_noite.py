#Bom dia e boa noite

n = int(input())
while True: 
    if n == 0:
        print('Ué? Já acabou?')
        break
    elif n % 2:
        print('Boa noite!')
    else:
        print('Bom dia!') 
    n -= 1