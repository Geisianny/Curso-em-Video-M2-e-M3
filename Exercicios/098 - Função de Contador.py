from time import sleep

def c(i,f,p):
    print('-='*20)
    print('Contagem de {} até {} de {} em {}'.format(i,f,p,p))
    if i < f:
        cont = i
        while cont <= f:
            print(cont ,end=' ')
            sleep(0.7)
            cont += p
        print('FIM!')
        
    else:
        cont = i
        while cont >= f:
            print(cont, end = ' ')
            sleep(0.7)
            cont = cont -p
        print('FIM!')
    print('-='*20)    
#PROGRAMA PRINCIPAL
c(1,10,1)
c(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim:  '))
p = int(input('Passo:  '))
c(i,f,p)


