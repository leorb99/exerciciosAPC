# Tesouro

s = input()
d = s.find('X') - s.find('P')          # calcula a distancia entre Pericles e o Tesouro
strAux1 = s[s.find('P'):s.find('X')+1] # string que mostra o que ha entre Pericles e o Tesouro 
strAux2 = s[s.find('X'):s.find('P')+1] # string que mostra o que ha entre o Tesouro e Pericles
if '#' in strAux1 or '#' in strAux2:   # se tiver algo entre Pericles e o tesouro ...
    print('Péricles esse caminho não funciona')
elif not 'X' in s:                     # se nao tiver tesouro ...  
    print('Péricles, não tem tesouro')
elif 'X' in s:                         # quantos passos para o tesouro
    print(f'Péricles, {d} passos')