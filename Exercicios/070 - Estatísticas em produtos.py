print("-"*30)
print("Loja super baratão")
print("-"*30)

total = 0
mil = 0
barato = 0
cont = 0
x = ' '
while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    total += preco
    cont += 1
    if(preco > 1000):
        mil += 1
    if cont == 1:
        menor = preco
        x = nome
    else:
        if preco < menor:
            menor = preco
            x = nome
    resp = ' '
    while resp not in 'SN':
         resp = input("Quer continuar? [S/N] ")
         break
    if resp == 'N':
        break
    
print("O total da compra foi R$ {}".format(total))
print("Temos {} produtos custando mais de R$ 1000.00".format(mil))
print("O produto mais barato foi {} que custou R${}".format(x,menor))
