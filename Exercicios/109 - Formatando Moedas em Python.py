from ex109 import moeda

p = float(input('digite o preço: R$:'))
print(f'a metade de {moeda(moeda(p))} é {moeda(metade(p))}')
print(f' o dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')

