def fatorial(n,show=False):
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('X',end=' ')
            else:
                print('=', end= ' ')
        f *= c
    return f


#Programa Principal
n = int(input('Digite um numero: '))
print(fatorial(n,show=True))
