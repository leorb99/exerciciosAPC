#Dêivis em fuga!

"""
le um int -> entra no looping -> enquanto x != -1
se x == 0 -> int -1
se x == 1 -> le outro x -> int + x
se x == 2 -> le y -> int - y
se o tanque > 0 -> count += 1
se l > tanque -> l = tanque
"""

l = int(input())
tanque = l
x = count = 0

while x != -1:                 
    if l >= 0:
        x = int(input())
        count += 1
        if x == 0:
            l -= 1
            #count += 1
        elif x == 1:
            x = int(input())
            l += x
            if l > tanque:
                l = tanque
        elif x == 2:
            y = int(input())
            l -= y
            #count += 1
    else:
        x = int(input())
if l >= 0:
    print('Lar Deivis lar')
else:
    print(count - 1)    


# 2         Lar Deivis lar
# 0
# 0
# -1    

# 87995     21
# 0
# 2
# 16679
# 1
# 61504
# 0
# 2
# 40712
# 1
# 66741
# 2
# 44761
# 0
# 2
# 9291
# 1
# 25898
# 0
# 0
# 2
# 35733
# 1
# 84824
# 1
# 25419
# 0
# 1
# 81046
# 1
# 76895
# 2
# 81225
# 0
# 1
# 59424
# 2
# 71417
# 2
# 83579
# 0
# 0
# 0
# 0
# 1
# 48738
# 0
# 0
# 0
# 0
# 1
# 65052
# 2
# 73585
# 1
# 36387
# 2
# 26971
# 0
# 1
# 23532
# 0
# 0
# 2
# 72664
# 1
# 43919
# 1
# 41588
# 1
# 4187
# 1
# 23983
# 0
# 2
# 38541
# 1
# 68851
# 2
# 7541
# 1
# 82847
# 0
# 1
# 81702
# 2
# 53440
# 0
# 0
# 0
# 1
# 3921
# 0
# 1
# 42085
# 2
# 55755
# 2
# 43539
# 2
# 60457
# 1
# 60263
# 1
# 65501
# 2
# 46751
# 2
# 44531
# 2
# 79311
# 2
# 56956
# 2
# 65569
# 1
# 11008
# 1
# 78907
# 0
# 2
# 41097
# 0
# -1


# 74516      10
# 0
# 0
# 1
# 65411
# 2
# 74510
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# -1

# while x != -1:
#     x = int(input())
#     if l >= 0:
#         count += 1 
#         if x == 0:
#             l -= 1
#         elif x == 1:
#             x = int(input())
#             l += x    
#             #print(l)
#             if l > tanque:
#                 l = tanque
#             #    print(l)
#         elif x == 2:
#             y = int(input())
#             l -= y
#         print(l)
# if l > 0:
#     print('Lar Deivis lar')
# else:
#     print(count)
