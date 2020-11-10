cont = ('zero', 'um', 'doid', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove','dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove','vinte')
num = 0
while True:    
    num = int(input("Digite um numero entre 0 e 20: "))
    if( num < 0 or num > 20):
        num = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    else:
        print("Você digitou o numero {}".format(cont[num]))
    resp = ' '
    while resp not in 'SN':
        resp = input("Você quer continuar [S/N] : ").upper().strip()
    if resp == 'N':
        break
print("{:=^30}".format('PROGRAMA FINALIZADO'))
        
