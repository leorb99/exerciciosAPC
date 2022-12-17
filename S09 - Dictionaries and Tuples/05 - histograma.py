# Histograma

# igual do livro
# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d
# print(histogram(h))

# meu proprio
string = input()
hist = {}

for char in string:
    hist[char] = string.count(char)
print((hist))