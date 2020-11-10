def metade(n= 0):
    return n/2
def dobro(n= 0):
    return n * 2
def aumento(n= 0,t=0):
    p = n +(n*t/100)
    return p
def desconto(n=0,t=0):
    p = n -(n*t/100)
    return p
def m(p = 0, m = 'R$'):
    return '{}{}'.format(m,p).replace('-',',')
