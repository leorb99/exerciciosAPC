# Lendo ate uma linha

n = int(input())

with open('poema.txt', 'r') as arquivo:
    for i in range(int(input())):
        linha = arquivo.readline().strip('\n')
        if linha == '':
            break
        else:
            print(linha)





# poema.txt
# Em certo reino um rei havia
# De nobre estirpe secular
# Que começou, um belo dia,
# Do pé direito capengar.
# Um calo enorme era o motivo
# Que dava ao rei um tal cacoete:
# Calo feroz, duro, agressivo,
# Plantado sobre o real joanete.
# Mas essa causa assim plebeia
# Ficava mal de publicar;
# E toda a corte teve a ideia
# De andar coxeando, a capengar.
# Príncipes, duques e marqueses,
# Viscondes, condes e barões
# Andavam, coxos e corteses,
# Com mil mesuras nos salões.
# Passou da corte à burguesia
# O modo esdrúxulo de andar.
# Vulgarizou-se a tal mania
# E andava o povo a capengar.
# Desde a nobreza solarenga
# Ao camponês da rude grei,
# Tudo no reino era capenga
# Para endossar o velho rei.
# E o rei sorria, satisfeito,
# Por ser benquisto e popular;
# Não era mais nenhum defeito,
# Naquele reino, o capengar.
# Mas eis que, um dia, um tipo surge,
# Em passo firme, andando bem;
# O povo, unânime, se insurge,
# E a corte a fúria não contém.
# Possessa, diz toda a cidade:
# ‒ Castigo dê-se-lhe, exemplar!
# Crime é de lesa-majestade
# Viver, aqui, sem capengar.
# É preso o infame; e logo o júri
# Se reúne ali dos cidadãos,
# Para que o crime, enfim, se apure,
# E o vil, da lei, caia nas mãos.
# E clama o júri: ‒ o reino insulta!
# O nosso rei tenta aviltar!
# E clama e freme a turbamulta,
# De um lado a outro, a capengar.
# Mas fala o réu: ‒ Por Jesus Cristo,
# Não me mandeis para as galés!
# Se ando direito é só por isto:
# Eu sou capenga dos dois pés...


