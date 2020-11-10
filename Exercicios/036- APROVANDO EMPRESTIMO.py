
valor = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
qnts_anos = int(input("Quantos anos de financiamento? "))

prestacao = valor/(qnts_anos * 12)
emprestimo = salario * 30/100

print("Para pagar uma casa de R$ {} em {} anos a prestação sera de R$ {:.2f} ".format(valor,qnts_anos,prestacao), end ='')
if(emprestimo >= prestacao):
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")
