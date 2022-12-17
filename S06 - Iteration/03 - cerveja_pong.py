#Cerveja Pong

#verificar se um numero eh primo
# n = int(input())
# aux = 0
# count = 1

# while aux <= (n // 2):
#     aux += 1
#     if n % aux == 0:
#         count += 1

# if n == 1:
#     print('Faina')
# elif count == 2 or n == 2:
#     print('Emidio')
# elif n == 1 or count != 2:
#     print('Faina')

number = int(input('Numero: '))
ePrimo = 0

for i in range(1, (number // 2)):        
    if number % i == 0:
        ePrimo += 1
    
if ePrimo == 1 :
    print('primo')
else:
    print('nao primo')
