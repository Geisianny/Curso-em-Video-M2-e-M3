res = 'S'

maior = 0
menor = 0
qnt = 0
media = 0
soma = 0
while(res == "S"):
    num = int(input("Digite um numero: "))
    soma += num
    qnt += 1
    if qnt == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input("Quer continuar? [S/N] "))
    media = soma / qnt
print("Voce digitou {} numeros e a media é {}".format(qnt, media))
print("O maior valor foi {} e o menor foi {}".format(maior,menor))
