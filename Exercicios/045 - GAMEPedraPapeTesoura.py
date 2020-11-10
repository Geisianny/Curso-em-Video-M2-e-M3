from random import randint

itens = ("Pedra", "papel", "tesoura")
computador = randint(0,2)

print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input("Qual é a sua jogada? "))
print("JO\nKEN\nPO !!!")
print("-="*10)
print("O computador jogou {}".format(itens[computador]))
print("Você jogou {}".format(itens[jogador]))
print("-="*11)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print("empate")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVALIDA!")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("empate")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVALIDA!")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("empate")
    else:
        print("JOGADA INVALIDA!")
