def leia_dinheiro(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.', 1)
        if entrada.replace('.', '', 1).isdigit():
            return float(entrada)
        print(f'\033[1;31mERRO! "{entrada}" é um preço inválido!\033[m')

def leiaInt(msg=''):
    while True:
        num = input(msg).strip()
        if num.replace('-', '', 1).isdigit():  # .isnumeric()
            return int(num)
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
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
    
    res = valor / 2
    return res if not formatc else moeda(res)


def moeda(valor=0., moeda='R$'):
    
    res = f'{moeda}{valor:.2f}'
    return res.replace('.', ',', 1) if moeda == 'R$' else res


def resumo(valor=0, aumento=0, reducao=0):
    
    print('-' * 32)
    print(f'|{"RESUMO DO VALOR":^30}|')
    print('-' * 32)
    print(f'| Preço analisado |  {moeda(valor):<9} |')
    print(f'| Metade do preço |  {metade(valor, True):<9} |')
    print(f'| Dobro do preço  |  {dobro(valor, True):<9} |')
    print(f'| {aumento:>3}% de aumento |  {aumentar(valor, aumento, True):<9} |')
    print(f'| {reducao:>3}% de redução |  {diminuir(valor, reducao, True):<9} |')
    print('-' * 32)    
