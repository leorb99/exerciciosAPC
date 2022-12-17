# Maior String

n = int(input())
maior = ''
for i in range(n):
    string = input()
    if len(maior) < len(string):
        maior = string
print(maior)