from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = 2020 - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input("Salario: "))
    dados['aposentadoria'] = dados['idade'] +((dados['contratação'] + 35)- datetime.now().year)
print("=-"*30)    
print(dados)

