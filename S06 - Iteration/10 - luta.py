#Luta
# for i in range (1 à d + 1)
# if i % k, l, m, n == 0 -> count += 1

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

count = 0
for i in range(1, d + 1):
    if (i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0):
        count += 1

print(count)