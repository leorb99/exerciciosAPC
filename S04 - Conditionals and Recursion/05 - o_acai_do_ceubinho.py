#O ACAI DO CEUBINHO
def qtdcopos(n):
    if n % 4:
        print(f'Pode voltar pro ceubinho, deivis! Falta(m) {4 - n % 4} copo(s)!')
    elif n == 0:
        print(f'Pode voltar pro ceubinho, deivis! Falta(m) 4 copo(s)!')
    else:
        print('Pode levar pros calourinhos, deivis!')
qtdcopos(8)
qtdcopos(15)
qtdcopos(0)