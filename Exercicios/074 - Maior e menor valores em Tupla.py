from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

for n in numeros:
    print(n,end= ' ')
print("\nO maior valor sorteado foi {}".format(max(numeros)))
print("O menor valor sorteado foi {}".format (min(numeros)))
