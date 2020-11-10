num = int(input("Digite um número inteiro: "))
print("escolha uma das bases para conversão: ")
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")
opc = int(input("Sua opção: "))

if(opc == 1):
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)))
elif(opc == 2):
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)))
else:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)))
