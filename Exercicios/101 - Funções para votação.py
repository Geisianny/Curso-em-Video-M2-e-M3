def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    
    if idade < 16:
        return 'Com {} anos: VOTO OBRIGATORIO.'.format(idade)
    elif 16<= idade < 18 or idade > 65:
        return 'Com {} anos: VOTO OPCIONAL.'.format(idade)
    else:
        return 'Com {} anos: NÃO VOTA.'.format(idade)

#Programa Principal
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
