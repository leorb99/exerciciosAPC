#ESCREVENDO DATAS
dia, mes, ano = map(int, input().split('/'))
print(f'{dia:02d}-{mes:02d}-{ano:02d}')
print(f'{mes:02d}-{dia:02d}-{ano:02d}')
print(f'{ano:02d}/{mes:02d}/{dia:02d}')