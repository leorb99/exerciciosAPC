# Palindromo

# o else vai comparar termo a termo entre 's' e 'invertido' 
# e contar quantos sao diferentes se count <= 2 -> print('ON')

s = input()
invertido = s[::-1]
count = 0
metade1 = s[:(len(s) // 2)]                 # metade da string digitada
metade2 = invertido[:(len(invertido) // 2)] # metade do inverso da string digitada
for i in range(len(s) // 2):                # for para comparar letras de cada metade
    if metade1[i] != metade2[i]:            # quando uma letra eh diferente count eh incrementado
        count += 1
if count <= 1:
    # se a palvra for um palindromo sem precisar trocar uma letra imprime 'OFF'
    if (metade1 == metade2) and (len(s) % 2 == 0):
        print('OFF')
    else:
        print('ON')
else: 
    print('OFF')

# abccaa      ON 
# abbcca      OFF
# glxlg       ON 
# fccf        OFF  
# abcda       ON
# ukvciu      OFF
