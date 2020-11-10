nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))

media =( nota1 + nota2)/2
print("Tirando {} e {}, a media do aluno é {:.1f}".format(nota1,nota2,media))

if( media < 5.0):
    print("O aluno está reprovado")
elif(media > 5.0 and media < 6.9):
    print("O aluno está recuperação")
else:
    print("O aluno está aprovado")
