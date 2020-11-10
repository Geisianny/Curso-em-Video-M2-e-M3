lista = []
resp = " "
while True:
    num = int(input("Digite um numero: "))
    if num not in lista:
       lista.append(num)
       print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! não irei adiciona-lo")
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "Nn":
        break
print("-="*30)
print("você digitou os valores {}".format(lista))
print("-="*30)
lista.sort()
print("-"*30)
print("Os valores ordenados são {}: ".format(lista))
print("-"*30)
