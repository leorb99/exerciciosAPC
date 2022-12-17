#PACOTES DE BOLACHA 2

def pacotesDeBolacha(m, n, k):
    if (k * n) > m:
        var = m // n
        print(f'{(var * n)}')
    else:
        print(f'{k * n}')
        
pacotesDeBolacha(4, 4, 1) # 4
pacotesDeBolacha(13, 5, 2) # 10 
pacotesDeBolacha(10, 9, 2) # 9 
pacotesDeBolacha(60, 20, 3) # 60
pacotesDeBolacha(4, 4, 1) # 4
pacotesDeBolacha(23, 6, 6) # 18
