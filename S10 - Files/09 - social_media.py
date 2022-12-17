# Social Media

from json import load

a = input()

with open(a) as arq:
    analise = load(arq)
    for i in range(len(analise['GraphImages'])):
        for n in analise['GraphImages'][i]:
            print(f'Publicacao numero {i + 1}')
            print(analise['GraphImages'][i]['username'])
            print(analise['GraphImages'][i]['edge_media_preview_like']['count'])
            break

# theydrawandcook.json
# Publicacao numero 1
# theydrawandcook
# 153
# Publicacao numero 2
# theydrawandcook
# 537
# Publicacao numero 3
# theydrawandcook
# 416
# Publicacao numero 4
# theydrawandcook
# 996
# Publicacao numero 5
# theydrawandcook
# 422
# Publicacao numero 6
# theydrawandcook
# 505
# Publicacao numero 7
# theydrawandcook
# 940
# Publicacao numero 8
# theydrawandcook
# 961
# Publicacao numero 9
# theydrawandcook
# 772
# Publicacao numero 10
# theydrawandcook
# 919

# teste.json
# Publicacao numero 1
# sharpycharot
# 6207
# Publicacao numero 2
# sharpycharot
# 10442
# Publicacao numero 3
# sharpycharot
# 8700
# Publicacao numero 4
# sharpycharot
# 10155
# Publicacao numero 5
# sharpycharot
# 14754
# Publicacao numero 6
# sharpycharot
# 14464
# Publicacao numero 7
# sharpycharot
# 26212
# Publicacao numero 8
# sharpycharot
# 37946
# Publicacao numero 9
# sharpycharot
# 11006
# Publicacao numero 10
# sharpycharot
# 11298



# monafinden.json
# Publicacao numero 1
# monafinden
# 16309
# Publicacao numero 2
# monafinden
# 26854
# Publicacao numero 3
# monafinden
# 13547
# Publicacao numero 4
# monafinden
# 14570
# Publicacao numero 5
# monafinden
# 13453
# Publicacao numero 6
# monafinden
# 11359
# Publicacao numero 7
# monafinden
# 8552
# Publicacao numero 8
# monafinden
# 17547
# Publicacao numero 9
# monafinden
# 8177
# Publicacao numero 10
# monafinden
# 18184