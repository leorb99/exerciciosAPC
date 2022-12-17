#Triângulo Descrescente

n = int(input())

for i in range(n, -1, -2):
    for j in range(i, -1, -2):
        print(j, end=' ')
    print()




""" 
n = int(input())

for i in range(n, -1, -2):
    for j in range(i, -1, -2):
        print(j, end=' ')
    print()
"""
""" 

n = int(input())
i = n
if n % 2 == 0:
    while n > 0:
        while i >= 0:
            print(n, end=' ')
            n -= 2
        i -= 2
        print()
        print(i, end=' ')
    print()
else:
    while i > 1:
        while n >= 0:
            print(n, end=' ')
            n -= 2
        i -= 2
        print() 
        print(i, end=' ')
    print()

"""
