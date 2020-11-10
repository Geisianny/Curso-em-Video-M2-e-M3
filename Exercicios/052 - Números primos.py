num = int(input("Digite um numero inteiro: "))

cont = 0
for i in range(1, num + 1):
    if(num % i == 0):
        cont += 1
if cont <= 2:
    print("{} é primo pois foi divisível {} vezes.".format(num, cont))
else:
    print("{} não é primo pois ele foi divisível {} vezes.".format(num,cont))
