# Onde esta Wally?

a = input()
horizontal = False
linhas = []
colunas = []
coluna = []

with open(a) as arq:
    for line in arq:
        linhas.append(line.strip('\n'))

    for i in range(len(linhas[0])):
        for j in range(len(linhas)):
            coluna.append(linhas[j][i])
        colunas.append(''.join(coluna))
        coluna.clear()
    
    for i in range(len(linhas)):
        if 'wally' in linhas[i]:
            print(i + 1, linhas[i].index('wally') + 1, 'horizontal')
            horizontal = True

    if horizontal == False:
        for i in range(len(colunas)):
            if 'wally' in colunas[i]:
                print(colunas[i].index('wally') + 1, i + 1, 'vertical')





# 0.txt
# jhrwallyli                                                                                                            
# ymqshnukup
# gnhkpfayqf
# dmrtfozdnb
# wdmcclijwh
# aroaztzipw
# nuowlmveps
# ffvgplddar
# shwcgrkuxu
# eyhxtpekdz

# 1.txt
# dxesfpsofd
# oegtyzswnl
# eiujzakumm
# mhiszifszt
# wallywxkyk
# dqwhzsbdxv
# tezzqbdzha
# lphpjttjye
# btdgekxqjz
# zysnclucib

# 2.txt
# cmlkjwsarrlqrgc
# psjfsiwpbkklrda
# pohxwjqpicofvss
# lrfunuyubnuauqf
# sbhepwdwkcplyaw
# evzhfajdaqgfvea
# amayilouwnduegs
# qhwmtlyhednvjli
# hwglwyltvgkeosn
# amssnfeuqpoeiyz
# phexcfwugbeitvd
# kwqkzydyqnmgikp
# craqjjxuhzzszuh
# pfgyvkdnlxohakz
# npwtwbhzuztkleo