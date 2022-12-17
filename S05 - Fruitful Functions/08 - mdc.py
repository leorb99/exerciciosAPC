#MDC

def mdc(a, b):
    if a > 0 and b > 0:
        return mdc(b, a % b)    
    return a

print(mdc(70, 25)) # 5
print(mdc(6,6)) #6
print(mdc(12,30)) #6
print(mdc(105,60)) #15

# n = int(input("Digite n: "))
# m = int(input("Digite m: "))
# resto = m % n
# while resto != 0:
#     resto = n % m
#     n = m
#     m = resto
#     print(n, m, resto)
# print("MDC(%d,%d)=%d" %(n,m,n))

