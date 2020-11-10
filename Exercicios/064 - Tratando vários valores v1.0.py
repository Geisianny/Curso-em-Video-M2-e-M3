num = 0
num = int(input("Digite um numero [999 para parar]: "))
cont = 0
soma = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um numero [999 para parar]: "))
print("você digitou {} numeros e a soma entre eles foi {}.".format(cont,soma))
