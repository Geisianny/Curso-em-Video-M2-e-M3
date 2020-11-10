
soma = 0
cont = 0
for i in range(1, 7):
    num = int(input("Digite um {} numero: ".format(i)))
    if(num % 2 == 0):
        soma += num
        cont += 1
print("voce informou {} números PARES e a soma foi {}".format(cont,soma))
