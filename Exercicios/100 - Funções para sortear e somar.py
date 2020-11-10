from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(n, end= ' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

def soma_par(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print('Somando os valores pares de {}, temos {}'.format(lista, soma))

#PROGRAMA PRINCIPAL
num = list()
sorteia(num)
soma_par(num)

