from time import sleep

def maior(*num):
    m = 0
    cont = 0
    print('-='*30)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(valor, end= ' ', flush =True)
        sleep(0.3)
        if cont == 0:
            m = valor
        else:
            if valor > m:
                m =valor
        cont += 1
    print('{}'.format(cont))
    print('o maior valor foi {}.'.format(m))

num = list
#PROGRAMA PRINCIPAL
print("-="*30)
print("Analisando os valores passados...")
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
