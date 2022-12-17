# Voltando para a biblioteca

biblioteca = {}

for i in range(5):
    livro = input()
    qtd = int(input())
    biblioteca[livro] = qtd
livro = input()
if livro in biblioteca:
    print(f'Achei! Temos {biblioteca[livro]} exemplar(es)!')
else:
    print('Poxa, não temos esse livro')
print(biblioteca)