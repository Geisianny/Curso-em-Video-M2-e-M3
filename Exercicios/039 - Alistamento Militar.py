from datetime import date

nasc = int(input("Digite o ano de nascimento: "))

atual = date.today().year
anos = atual - nasc

print("quem nasceu em {} tem {} anos em {}".format(nasc,anos, atual))
if(anos < 18):
    saldo = 18 - anos
    print("voce ainda não tem 18 anos. Ainda faltam {} anos para o alistamento".format(saldo))        
elif(anos == 18):
    print("voce tem que se alistar IMEDIATAMENTE!")
elif(anos > 18):
    saldo =  anos - 18
    print(" voce ja deveria ter se alistado há {} anos".format(saldo))
    
