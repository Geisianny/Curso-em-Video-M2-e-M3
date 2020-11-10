lista = []
tem = []
mai = 0
men = 0
while True:
    tem.append(str(input('Nome: ')))
    tem.append( float(input('Peso: ')))
    if len(lista) == 0:
        mai = men
        men = tem[1]
    else:
        if tem[1] > mai:
            mai = tem[1]
        if tem[1] < men:
            men = tem[1]
    lista.append(tem[:])
    tem.clear()
    resp = str(input("Quer continuar:[S/N] "))
    if resp in 'Nn':
        break
print("-"*30)
print("Ao todo, você cadastrou {} pessoas.".format(len(lista)))
print("O maior peso foi de {} kg .Peso de ".format(mai))
for p in lista:
    if p[1] == mai:
        print("[{}]".format(p[0]), end='')
print()
print("O menor peso foi de {} kg .Peso de ".format(men))
for p in lista:
    if p[1]== men:
        print("[{}]".format(p[0]), end='')
print()



    
    
