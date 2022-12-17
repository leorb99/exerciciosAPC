#BANNER
def banner(n):
    if n > 0 and not(n % 2):
        print('| | | | | | | | | |')
    elif n > 0 and n % 2:
        print('- - - - - - - - - -')
    elif n < 0 and not(n % 2):
        print('. . . . . . . . . .') 
    else:
        print('= = = = = = = = = =')
banner(1)
banner(2)
banner(-1)
banner(-2)