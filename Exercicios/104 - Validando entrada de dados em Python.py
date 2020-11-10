def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO!Digite um numero inteiro valido.')
        if ok:
            break
    return valor
  
#Programa principal
n = leiaint('Digite um  numero: ')
print('Você acabou de digitar o numero {}'.format(n))
