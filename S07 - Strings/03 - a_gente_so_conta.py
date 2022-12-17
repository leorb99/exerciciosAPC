# A gente so conta

a, string = input().split()
count = 0
for letter in string:
    if letter == a:
        count += 1
print(count)