# Anagrama

s = input()
t = input()

def histograma(s):
    hist = {}
    for char in s:
        hist[char] = s.count(char)
    return hist

if histograma(s) == histograma(t):
    print(True)
else:
    print(False)