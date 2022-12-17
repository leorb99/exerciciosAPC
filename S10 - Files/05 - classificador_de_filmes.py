# Classificador de filmes

genero = input().capitalize()
duracao = int(input())
nao_tem = False

with open('filmes.txt') as arq:
    for linha in arq:
        linha = linha.strip('\n')
        linha = linha.split('/')
        if genero in linha and int(linha[2]) <= duracao:
            print(linha[0])
            nao_tem = True

if nao_tem == False:
    print('Não foram encontrados filmes assim')
	

# filmes.txt
# Um Sonho de Liberdade/Drama/144
# O Poderoso Chefão/Drama/175
# O Poderoso Chefão II/Drama/202
# Batman: O Cavaleiro das Trevas/Ação/152
# 12 Homens e uma Sentença/Drama/156
# A Lista de Schindler/Drama/195
# O Senhor dos Anéis: O Retorno do Rei/Aventura/201
# Pulp Fiction: Tempo de Violência/Drama/154
# Três Homens em Conflito/Western/161
# O Senhor dos Anéis: A Sociedade do Anel/Aventura/178
# Clube da Luta/Drama/139
# Forrest Gump: O Contador de Histórias/Drama/142
# A Origem/Ação/148
# O Senhor dos Anéis: As Duas Torres/Aventura/179
# Star Wars, Episódio V: O Império Contra-Ataca/Fantasia/124
# Matrix/Ação/136
# Os Bons Companheiros/Drama/146
# Um Estranho no Ninho/Drama/133
# Os Sete Samurais/Ação/207
# Seven: Os Sete Crimes Capitais/Mistério/127
# O Silêncio dos Inocentes/Suspense/118
# Cidade de Deus/Drama/130
# A Vida é Bela/Comédia/116
# A Felicidade Não se Compra/Drama/130
# Guerra nas Estrelas/Fantasia/121
# O Resgate do Soldado Ryan/Drama/169
# Interestelar/Ficção Científica/169
# A Viagem de Chihiro/Animação/125
# À Espera de um Milagre/Drama/189
# Parasita/Suspense/132
# O Profissional/Ação/170
# Harakiri/Ação/133
# O Pianista/Drama/150
# Os Suspeitos/Mistério/166
# O Exterminador do futuro 2: O julgamento final/Ação/137
# De Volta para o Futuro/Aventura/176
# Psicose/Terror/109
# O Rei Leão/Animação/98
# Tempos Modernos/Comédia/97
# A Outra História Americana/Drama/179
# Luzes da Cidade/Comédia/97
# Túmulo dos Vagalumes/Animação/99
# Whiplash: Em Busca da Perfeição/Drama/106
# Gladiador/Ação/155
# Os Infiltrados/Suspense/151
# Intocáveis/Comédia/112
# O Grande Truque/Mistério/130
# Casablanca/Drama/102
# Era uma Vez no Oeste/Western/165
# Janela Indiscreta/Mistério/112
# Cinema Paradiso/Romance/155
# Alien - O 8º Passageiro/Terror/117