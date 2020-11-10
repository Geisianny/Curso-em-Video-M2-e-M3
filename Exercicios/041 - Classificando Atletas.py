from datetime import date

nasc = int(input("Digite o ano de nascimento: "))
atual = date.today().year

ano = atual - nasc

print("O atleta tem {} anos.".format(ano))

if(ano <=9):
    print("Classificação: MIRIM")
elif( ano > 9 and ano <= 14):
    print("Classificação: INFANTIL")
elif(ano > 14 and ano<=19):
    print("Classifição: JÚNIOR")
elif(ano > 19 and ano <= 25):
    print("Classifição: SÊNIOR")
else:
    print("Classifição: MASTER")
