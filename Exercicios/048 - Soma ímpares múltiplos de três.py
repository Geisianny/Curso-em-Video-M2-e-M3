soma = 0
cont = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        soma += i
        cont += 1
print("A soma de todos os {} valore solicitados é {}".format(cont,soma))
