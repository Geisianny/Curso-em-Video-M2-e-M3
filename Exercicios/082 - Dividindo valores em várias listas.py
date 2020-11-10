lista = []

while True:
    num = int(input("Digite um numero: "))
    lista.append(num)
    resp = str(input("Quer continuar? [S/N]"))
    if resp in 'Nn':
        break
par = []
impar = []
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print("-"*30)
print("A lista completa é {}".format(lista))
print("A lista de pares é {}".format(par))
print("A lista de impares é {}".format(impar))
print("-"*30)
    
