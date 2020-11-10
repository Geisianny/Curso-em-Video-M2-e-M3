from random import randint

print("Sou seu computador...")
print("acabei de pensar em um numero entre 0 e 10.")
print("Será que voce consegue adivinhar qual foi? ")
usuario = int(input("Qual é seu palpite? "))

computador = randint(0,10)

cont = 1
while(usuario != computador):
    usuario = int(input("Qual é seu palpite? "))
    cont = cont + 1
                  
print("voce acertou!, vc precisou de {} vezes para acertar!".format(cont))
