# Consultas de intervalo na string 1

q = int(input())

for i in range(q):
    l, r, s = input().split()
    l = int(l)
    r = int(r)
    if l == 0:
        print(s[r:l:-1] + s[0])
    else:
        print(s[r:l-1:-1])

    
frase = 'noiprocSsVoreZbuS'
print(frase[16:9:-1])