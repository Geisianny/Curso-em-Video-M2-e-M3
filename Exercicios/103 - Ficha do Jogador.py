def ficha(jog= '<desconhecido',gol=0):
    print('O jogador {} fez {} gol(s) no campeonato.'.format(jog,gol))

#programa principal

nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome,gols)
