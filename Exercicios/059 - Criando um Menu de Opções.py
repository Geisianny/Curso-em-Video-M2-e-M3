num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))


res = 0
opc = 0

while(opc != 5):
    print("""    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa""")
    opc = int(input(">>>> Qual é a sua opção: "))
    if(opc == 1):
        res = num1 + num2
        print("soma de {} e {} = {}".format(num1, num2, res))
    elif(opc == 2):
        res = num1 * num2
        print("Multiplicao de {} e {} = {}".format(num1, num2, res))
    elif(opc == 3):
        if( num1 > num2):
            print("{} é maior".format(num1))
        else:
            print("{} é maior".format(num2))
    elif(opc == 4):
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))

print("Fim do programa! volte sempre!")

