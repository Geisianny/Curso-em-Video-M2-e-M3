valor = float(input(" Digite o valor do produto: "))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")

res = int(input("Qual é a opção? "))

if( res == 1):
    total =   valor - (valor* 10/100)
    print("Sua compra de R${} vai custa R${} no final.".format(valor, total))
elif(res == 2):
    total = valor - (valor* 5/100)
    print("Sua compra de R${} vai custa R${} no final.".format(valor, total))
elif(res == 3):
    total = valor
    print("sua compra de R${} vai ser parcela em 2 vezes de {} custando no final R${}.".format(valor, total/2, total))
else:
    p = int(input("Quantas parcelas? "))
    total = (valor*20/100) + valor
    print("Sua compra de R${} vai ser parcela em {} vezes de {} custando no final R${}.".format(valor, p,total/p, total))
