# Jogo da velha II

def jogoTerminou(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    if matriz[0] == matriz[1] == matriz[2] and matriz[0][0] == ' - ':
        return 0
    vencedor = False
    deuVelha = False
    for i in range(lin):
        if (matriz[i] == [' X ', ' X ', ' X ']) or (matriz[i] == [' O ', ' O ', ' O ']):
            vencedor = True  
        elif (matriz[0][0] == matriz[1][1] == matriz[2][2]) or (matriz[0][2] == matriz[1][1] == matriz[2][0]):
            vencedor = True
        elif matriz[0][i] == matriz[1][i] == matriz[2][i]:
            vencedor = True
        else:
            deuVelha = True
    if vencedor == True:
        return 1
    elif deuVelha == True:
        return 2

matriz = [[' - ', ' - ', ' - '], 
          [' - ', ' - ', ' - '], 
          [' - ', ' - ', ' - ']]
print(jogoTerminou(matriz))

matriz = [[' X ', ' X ', ' - '], 
          [' O ', ' O ', ' - '], 
          [' X ', ' X ', ' X ']]
print(jogoTerminou(matriz))

matriz = [[' X ', ' X ', ' O '], 
          [' - ', ' - ', ' O '], 
          [' X ', ' X ', ' O ']]
print(jogoTerminou(matriz))

matriz = [[' X ', ' O ', ' O '], 
          [' O ', ' O ', ' - '], 
          [' O ', ' - ', ' X ']]
print(jogoTerminou(matriz))

matriz = [[' X ', ' X ', ' O '], 
          [' O ', ' O ', ' X '], 
          [' X ', ' O ', ' X ']]
print(jogoTerminou(matriz))

