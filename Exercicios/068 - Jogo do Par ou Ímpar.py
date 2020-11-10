from random import randint

v = 0
print("=-"*20)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-"*20)
while True:
    num = int(input("Diga um valor: "))
    computador = randint(0,10)
    total = num + computador
    jogo = ' '
    while jogo not in 'PI':
        jogo = input("Par ou Ímpar? [P/I]").strip().upper()
    print("Você jogou {} e o computador jogou {}.Total de {}".format(num,computador,total))
    print("DEU PAR" if total % 2 == 0 else "Deu impar")
    if jogo == 'P':
        if total % 2 == 0:
            print("voce Venceu!")
            v += 1
        else:
            print("voce Perdeu!")
            break
    elif jogo == 'I':
        if total % 2 == 1:
            print("Você venceu!")
            v += 1
        else:
            print("Voce perdeu!")
            break
    print("Vamos jogar novamente...")
print("GAME OVER! voce venceu {} vezes".format(v))
            
