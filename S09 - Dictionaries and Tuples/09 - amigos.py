# Amigos

# amizade = {}
# n, p = map(int, input().split())
# alunos = input().split()

# for i in range(n):
#     amizade[alunos[i]] = []

# for i in range(p):
#     amigos = input().split()
#     if amigos[1] in amizade[amigos[0]] or amigos[0] in amizade[amigos[1]]:
#         continue
#     amizade[amigos[0]].append(amigos[1])
#     amizade[amigos[1]].append(amigos[0])

# aux = amizade.copy()

# for k in amizade:
#     for c in aux:
#         if k != c:
#             for i in range(len(amizade[k])):
#                 if amizade[k][i] in aux[c]:
#                     if c in amizade[k] or k in amizade[c]:
#                         continue
#                     amizade[k].append(c)
#                     amizade[c].append(k)

# for k in sorted(amizade):
#     print(f'{k} possui {len(amizade[k])} amigos')

# 5 3
# João Maria Miriam Pedro Matheus
# João Pedro
# Maria Miriam
# Pedro Matheus

# 4 2
# João Pedro Maria Miriam
# João Pedro
# Maria Miriam

# 3 2
# João Maria Miriam
# João Maria
# Maria Miriam

# 10 5
# Bruni Batatinha Brad Chef Tom Felix João Maria Mia Shawn
# Chef Brad
# Maria Tom
# Bruni Maria
# Bruni Mia
# Chef Shawn

# 10 8
# Mango Banana Guerreira Dune João Frajola Greg Xena Fifi Criss
# Mango Frajola
# Fifi Dune
# Xena Mango
# Xena Banana
# Banana Criss
# Mango Greg
# Criss Mango
# Fifi João

# 15 10
# Kiwi Greg Bruna Hunter Khali Mandachuva Luna Didi Matheus Maria João Lary Gatinho Bob Xanim
# Mandachuva Xanim
# Didi Greg
# João Bruna
# Gatinho Khali
# Kiwi Bruna
# Gatinho Luna
# Gatinho Mandachuva
# Matheus Mandachuva
# Hunter Bruna
# Kiwi Khali

# 25 15
# George Khali Felix Fifi Bambi Bichano Hunter Joao Mandachuva Vitor Thiago Breno Banana Lary Bob Xavier Helix Kiwi Bah Bruna Criss Gary Bolo Tom Buni
# Bolo Kiwi 
# Kiwi Bruna 
# Bichano Gary
# Xavier George
# Bichano Thiago 
# Khali Fifi
# Bambi Breno
# Helix Bichano
# Hunter Khali 
# Bob George
# George Tom
# Tom Banana
# Helix Felix
# Joao Vitor
# Bichano Xavier
# 
# 15 15
# Batatinha Luna Paco Buni Matheus Gus Docinho Bob Mandachuva Lary Chef Khali Shawn Morango Bruna
# Docinho Mandachuva
# Matheus Chef
# Chef Bruna
# Chef Matheus
# Bob Batatinha
# Docinho Matheus
# Khali Buni
# Luna Matheus
# Mandachuva Bob
# Luna Buni
# Morango Chef
# Paco Docinho
# Docinho Gus
# Bob Gus
# Luna Docinho

# 15 20
# Greg Breno Bruni Bambi Joao Gary Khali Docinho Kiwi Xavier Maria Tom Pedro Mia George
# Docinho Bambi
# Khali Mia 
# Bruni Tom
# Xavier Bambi
# George Joao
# Bambi Breno
# George Gary
# Greg Joao
# Bruni Docinho
# Mia George
# Maria Bruni
# Docinho Gary 
# Mia Bruni
# Tom Mia
# Joao Docinho
# Gary Docinho
# Bruni Greg
# Kiwi Gary
# Gary Breno
# Greg Maria

# 25 20
# Dune Gabriel Mandachuva Buni Docinho Lindinha Gus Guerreira Chef Khali Xanim Vitor Didi Bichano Felix Miriam Gary Joao Thiago Criss George Brad Bah Bolo Morango
# Bolo Dune
# Criss Khali
# Dune Brad
# Miriam Lindinha
# Thiago Gus
# Joao Bah
# Docinho Criss
# Criss Mandachuva
# Bah Criss 
# George Buni 
# Docinho Joao
# Brad Khali
# Lindinha Felix
# Gus Mandachuva
# Gary Miriam 
# Morango Felix
# Khali Gabriel
# Criss Bah 
# Miriam Vitor
# Miriam Dune

















# pega o primeiro valor da chave e vai ate a chave com mesmo nome 
# e add todos valores dessa chave exceto quem ja esta e o proprio nome da chave 
# ou add tudo e remove um na hr de imprimir

amizade = {}
n, p = map(int, input().split())
alunos = input().split()

for i in range(n):
    amizade[alunos[i]] = []

for i in range(p):
    amigos = input().split()
    if amigos[1] in amizade[amigos[0]] or amigos[0] in amizade[amigos[1]]:
        continue
    amizade[amigos[0]].append(amigos[1])
    amizade[amigos[1]].append(amigos[0])

aux = amizade.copy()

for k in amizade:
    for c in aux:
        for i in range(len(amizade[k])):
            for j in range(len(aux[c])):
                if amizade[k][i] == c and aux[c][j] not in amizade[k]:
                        amizade[k].append(aux[c][j])

print(amizade)

for k in sorted(amizade):
    if len(amizade[k]) > 0:
        print(f'{k} possui {len(amizade[k]) - 1} amigos')
    else:
        print(f'{k} possui {len(amizade[k])} amigos')



    # {
    # 'Greg': ['Joao', 'Bruni', 'Maria'], 
    # 'Breno': ['Bambi', 'Gary'], 
    # 'Bruni': ['Tom', 'Docinho', 'Maria', 'Mia', 'Greg'], 
    # 'Bambi': ['Docinho', 'Xavier', 'Breno'], 
    # 'Joao': ['George', 'Greg', 'Docinho'], 
    # 'Gary': ['George', 'Docinho', 'Kiwi', 'Breno'], 
    # 'Khali': ['Mia'], 
    # 'Docinho': ['Bambi', 'Bruni', 'Gary', 'Joao'], 
    # 'Kiwi': ['Gary'], 
    # 'Xavier': ['Bambi'], 
    # 'Maria': ['Bruni', 'Greg'], 
    # 'Tom': ['Bruni', 'Mia'], 
    # 'Pedro': [], 
    # 'Mia': ['Khali', 'George', 'Bruni', 'Tom'], 
    # 'George': ['Joao', 'Gary', 'Mia']
    # }


    # {
    # 'Greg': ['Joao', 'Bruni', 'Maria', 'Docinho', 'Tom', 'Mia', 'George', 'Bambi', 'Gary', 'Khali', 'Kiwi', 'Xavier'], 
    # 'Breno': ['Bambi', 'Gary', 'Docinho', 'Kiwi', 'Xavier', 'George', 'Bruni', 'Joao', 'Khali', 'Maria', 'Tom', 'Mia'], 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # 'Bruni': ['Tom', 'Docinho', 'Maria', 'Mia', 'Greg', 'Breno', 'Bambi', 'Joao', 'Gary', 'Khali', 'Kiwi', 'Xavier', 'George'], 'Bambi': ['Docinho', 'Xavier', 'Breno', 'Bruni', 'Greg', 'Joao', 'Gary', 'Khali', 'Kiwi', 'Maria', 'Tom', 'Mia', 'George'], 'Joao': ['George', 'Greg', 'Docinho', 'Bruni', 'Bambi', 'Breno', 'Gary', 'Khali', 'Kiwi', 'Xavier', 'Maria', 'Tom', 'Mia'], 'Gary': ['George', 'Docinho', 'Kiwi', 'Breno', 'Bruni', 'Bambi', 'Joao', 'Greg', 'Khali', 'Xavier', 'Maria', 'Tom', 'Mia'], 'Khali': ['Mia', 'Bruni', 'Bambi', 'Joao', 'Gary', 'Greg', 'Breno', 'Docinho', 'Kiwi', 'Xavier', 'Maria', 'Tom', 'George'], 'Docinho': ['Bambi', 'Bruni', 'Gary', 'Joao', 'Greg', 'Breno', 'Khali', 'Kiwi', 'Xavier', 'Maria', 'Tom', 'Mia', 'George'], 'Kiwi': ['Gary', 'Breno', 'Bruni', 'Bambi', 'Joao', 'Khali', 'Docinho', 'Greg', 'Xavier', 'Maria', 'Tom', 'Mia', 'George'], 'Xavier': ['Bambi', 'Breno', 'Bruni', 'Joao', 'Gary', 'Khali', 'Docinho', 'Kiwi', 'Greg', 'Maria', 'Tom', 'Mia', 'George'], 'Maria': ['Bruni', 'Greg', 'Bambi', 'Joao', 'Gary', 'Khali', 'Docinho', 'Kiwi', 'Xavier', 'Breno', 'Tom', 'Mia', 'George'], 'Tom': ['Bruni', 'Mia', 'Greg', 'Bambi', 'Joao', 'Gary', 'Khali', 'Docinho', 'Kiwi', 'Xavier', 'Maria', 'Breno', 'George'], 'Pedro': [], 'Mia': ['Khali', 'George', 'Bruni', 'Tom', 'Greg', 'Bambi', 'Joao', 'Gary', 'Docinho', 'Kiwi', 'Xavier', 'Maria', 'Breno'], 'George': ['Joao', 'Gary', 'Mia', 'Greg', 'Breno', 'Bruni', 'Bambi', 'Khali', 'Docinho', 'Kiwi', 'Xavier', 'Maria', 'Tom']}