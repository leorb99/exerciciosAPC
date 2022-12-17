# Substring ou nao

str1 = input()
str2 = input()

if str2 == str1:
    print('São iguais!')
elif str2 in str1:
    print('A segunda é uma substring da primeira')
elif str1 in str2:
    print('A primeira é uma substring da segunda')
else:
    print('São diferentes demais!')