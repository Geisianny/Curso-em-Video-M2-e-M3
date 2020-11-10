somaid = 0
mediaid = 0
maioridhomem = 0
nomevelho = ''

for i in range(1, 5):
    print("-"*5,"{}ª PESSOA".format(i),"-"*5)
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip()
    somaid += idade
    if i == 1 and sexo in 'Mm':
        maioridhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridhomem:
        maioridhomem = idade
        nomevelho = nome
        
mediaid = somaid/4
print("A média de idade do grupo é de {} anos".format(mediaid))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridhomem, nomevelho))
