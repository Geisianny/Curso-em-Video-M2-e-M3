import moeda1

preço = float(input('Digite um preço: R$'))
print(f'A metade de {moeda1.moeda1(preço)} é {moeda1.metade(preço, True)}')
print(f'O dobro de {moeda1.moeda1(preço)} é {moeda1.dobro(preço, True)}')
print(f'Aumentando 10%, temos {moeda1.aumentar(preço, 10, True)}')
print(f'Diminuindo 13%, temos {moeda1.diminuir(preço, 13, True)}')
