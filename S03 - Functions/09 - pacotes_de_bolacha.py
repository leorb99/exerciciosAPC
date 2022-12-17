#PACOTES DE BOLACHA 1

def pacotesDeBolacha(m, n, k):
    if (k * n) > m:
        var = m // n
        print(f'{m - (var * n)}')
    else:
        print(f'{m - k * n}')
'''
def pacotesDeBolacha(m, n, k):
    var = m // n
    print(f'{m - (var * n)}')
'''
pacotesDeBolacha(4,4,1) # 0 
pacotesDeBolacha(13,5,2) # 3 
pacotesDeBolacha(10,9,2) # 1 
pacotesDeBolacha(60,20,3) # 0
pacotesDeBolacha(4,4,1) # 0
pacotesDeBolacha(23,6,6) # 5
pacotesDeBolacha(2100, 440, 65) # 340
pacotesDeBolacha(10000, 1, 1) # 9999
pacotesDeBolacha(10000, 10000, 10000) # 0
pacotesDeBolacha(10, 5, 10000) # 0