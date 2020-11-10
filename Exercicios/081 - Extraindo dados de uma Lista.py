lista = []
resp = ' '
while True:
    num = int(input("Digite um valor: "))
    lista.append(lista)
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "Nn":
        break
print("Você digitou {} elementos.".format(len(lista)))
lista.sort( reverse=True)
print("Os valores em ordem decrescente são {}".format(lista))
if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista!")
