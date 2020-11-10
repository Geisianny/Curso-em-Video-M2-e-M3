def area(l,c):
   return l * c
    

#programa principal

print('Contole de terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO(m): '))

print("A area de um terreno {}x{} é de {}m².".format(l,c, area(l,c)))
