#TERMOS DA SEQUENCIA V1
#FICOU FEIO, MAS TO COM SONO, PERDOA
def imprimeTermos(n):
    if n == 2 or n == 1:
        print(n)
        print(n * 0)
    else:
        print(n)
        imprimeTermos(n - 2)
imprimeTermos(11)
imprimeTermos(8)
imprimeTermos(15)