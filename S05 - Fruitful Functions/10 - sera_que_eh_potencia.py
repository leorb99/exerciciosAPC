#SERA QUE EH POTENCIA

from math import *

def acredita(n1, n2):
    logaritmo = log(n1)/log(n2) #calcula log de n1 na base n2
    if logaritmo == round(logaritmo): #int no lugar de round provavelmente tbm funciona
        return 'Pode Acreditar'
    return 'Fake News'
print(acredita(8,2)) #Pode Acreditar
print(acredita(18,3)) #Fake News
print(acredita(625,5)) #Pode Acreditar
print(acredita(262144, 8)) #pdc
