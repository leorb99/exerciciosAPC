#CANETRINCAS

#MDC (p, v, a)
def mdc(p, v):
    if p > 0 and v > 0:
        return mdc(v, p % v)    
    return p

def calculaCaixa(p, v, a):
    return mdc(mdc(p, v), a)    

print(calculaCaixa(12,16,4)) #4
print(calculaCaixa(7, 31, 51)) #1
print(calculaCaixa(10, 100, 1000)) #10
print(calculaCaixa(9, 27, 81)) #9
print(calculaCaixa(45, 180, 9000)) #45
print(calculaCaixa(49, 777, 140)) #7
print(calculaCaixa(25,25,25)) #25