# Arquivo matematico

s = input()

with open(s) as arq:
    num1 = int(arq.readline().strip('\n'))
    char = arq.readline().strip('\n')
    num2 = int(arq.readline().strip('\n'))
    if char == '+':
        print(int(num1 + num2))
    elif char == '-':
        print(int(num1 - num2))
    elif char == '*':
        print(int(num1 * num2))
    elif char == '/':
        print(int(num1 / num2))
    elif char == '%':
        print(int(num1 % num2))

# a.txt
# 42
# /
# 2

# b.txt
# 2
# *
# 8

# c.txt
# 319847
# %
# 1237