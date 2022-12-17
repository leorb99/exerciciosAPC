# Jogo da velha I

def imprimeJogo(matriz):
    lin = matriz
    col = matriz[0]
    for i in range(len(lin)):
        for j in range(len(col)):
            print(matriz[i][j], end='')
        print()

def atualizaMatriz(matriz, lin, col, tipo):
    matriz[lin][col] = tipo
    return matriz

matriz = [[' - ', ' - ', ' - '], 
          [' - ', ' - ', ' - '], 
          [' - ', ' - ', ' - ']]
imprimeJogo(matriz)
print()
matriz = [[' - ', ' X ', ' - '], 
          [' - ', ' O ', ' - '], 
          [' - ', ' X ', ' - ']]
imprimeJogo(matriz)
print()
matriz = [[' - ', ' - ', ' - '], 
          [' - ', ' - ', ' - '], 
          [' - ', ' - ', ' - ']]
imprimeJogo(atualizaMatriz(matriz, 0, 1, ' X '))