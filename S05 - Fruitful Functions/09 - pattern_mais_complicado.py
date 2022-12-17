#PATTERN MAIS COMPLICADO

def pattern(n):
    if n > 0:
        if n % 2 == 0: 
            print(n)
            pattern(n - 5)
        else:
            print(n)
            pattern(n // 2)
    return print(n)

pattern(22)
print('\n')
pattern(64)
print('\n')
pattern(7)
print('\n')
#pattern(1000000)