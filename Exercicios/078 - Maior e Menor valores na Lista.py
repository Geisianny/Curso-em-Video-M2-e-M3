lista = []

for i in range(0,4):
        num = int(input(f"Digite um numero para a posição {i}: "))
        lista.append(num)
maximo = max(lista)
minimo = min(lista)
print("O maior valor é {} e está na posicao {}".format(maximo, lista.index(maximo)))
print("O menor valor a {} e está na posicao {}".format(minimo, lista.index(minimo)))
