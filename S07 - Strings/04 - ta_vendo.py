# Ta vendo?

s = input()
count = 0
fim = ' '

for letra in s:
    if letra == ' ':
        count += 1
    else:
        if count == 1 or count == 2:
            print(0)
        elif count > 2:
            print(count - 2)
        count = 0
    fim = letra