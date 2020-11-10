peso = float(input("Digite o peso: "))
h = float(input("Digite a altura: "))

imc = peso/ (h ** 2)

print("O IMC dessa pessoa é de {:.1f}".format(imc))
if(imc <18.5):
    print("Você esta abaixo do Peso.")
elif(imc > 18.5 and imc <= 25):
    print("PARABENS! você esta no peso ideal.")
elif(imc > 25 and imc <= 30):
    print("Você está com sobrepeso.")
elif (imc > 30 and imc <= 40):
    print("Você está com obesidade.")
else:
    print("Você esta com obesidade morbida.")
