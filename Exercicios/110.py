def aumentar(valor=0, taxa=0, formatc=False):
    
    res = valor + (valor * (taxa / 100))
    return res if formatc is False else moeda(res)


def diminuir(valor=0, taxa=0, formatc=False):
    
    res = valor - (valor * (taxa / 100))
    return res if formatc is False else moeda(res)


def dobro(valor=0, formatc=False):
    
    res = valor * 2
    return res if not formatc else moeda(res)


def metade(valor=0, formatc=False):
    
    print('-' * 32)
    print('|', 'RESUMO DO VALOR'.center(28), '|')  # print(f'|{"RESUMO DO VALOR":^30}|')
    print('-' * 32)
    print(f'| Preço analisado |  {moeda(valor):<9} |')
    print(f'| Metade do preço |  {metade(valor, True):<9} |')
    print(f'| Dobro do preço  |  {dobro(valor, True):<9} |')
    print(f'| {aumento:>3}% de aumento |  {aumentar(valor, aumento, True):<9} |')
    print(f'| {reducao:>3}% de redução |  {diminuir(valor, reducao, True):<9} |')
    print('-' * 32)

