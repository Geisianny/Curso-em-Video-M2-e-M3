
soma = 0
i = 0
while True:
    num = int(input("Digite um valor(999 para parar): "))
    if(num == 999):
        break
    soma += num
    i += 1
print("A soma dos {} valores foi {}!".format(i,soma))
