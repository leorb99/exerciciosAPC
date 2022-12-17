# Pares Bonitos

n = int(input())
a = list(map(int, input().split()))
count = 0

for num in a:
    for i in range(len(a)):
        if num * 2 == a[i] or a[i] * 2 == num:
            count += 1
print(int(count / 2))