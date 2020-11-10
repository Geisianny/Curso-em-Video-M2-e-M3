                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
cont18 = 0
contf = 0
contm = 0
cont20 = 0
while True:
    print("-"* 20)
    print("CADASTRE UMA PESSOA")
    print("-"* 20)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input("Sexo [M/F]  ").strip().upper()
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        contm += 1
    if sexo == 'F' and idade < 20:
        cont20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = input("Quer continuar? [S/N] ").strip().upper()
    if(resp == 'N'):
        break
    
print("Total de pessoas com mais de 18 anos: {}".format(cont18))
print("Ao todo temos {} homens cadastrados".format(contm))
print("E temos {} mulheres com menos de 20 anos".format(cont20))
