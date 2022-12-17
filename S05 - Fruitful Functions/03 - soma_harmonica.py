#SOMA HARMONICA

def soma_harmonica(X):
    if X == 1:
        return 1 * X
    return 1/X + soma_harmonica(X - 1)
print(soma_harmonica(6)) #2.4499999999999997
print(soma_harmonica(5)) #2.283333333333333 
print(soma_harmonica(2)) #1.5

