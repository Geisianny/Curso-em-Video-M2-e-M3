di = dict()
partidas = list()
time = list()
total = 0
while True:
    di['nome'] = str(input("Nome do Jogador: "))
    vezes = int(input('Quantas partidas {} jogou? '.format(di['nome'])))
    for i in range(0,vezes):
        partidas.append( int(input("Quantos gols na partida {}: ".format(i+1))))
    for i in partidas:
        total += int(i)
    di['partidas'] = partidas[:]
    di['total'] = total
    time.append(di.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in di.keys():
    print('{:<15}'.format(i), end='')
print()
print('-'*40)
for k,v in enumerate(time):
    print('{:>3} '.format(k),end='')
    for d in v.values():
        print('{:<15}'.format(str(d)),end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe jogador com codigo {}!'.format(busca))
    else:
        print('-- levantamento do jogador {}:'.format (time[busca]['nome']))
        for i,g in enumerate(time[busca]['partidas']):
            print('      No jogo {} fez {} gols.'.format(i+1,g))
    print('-'*40)
print('<< VOLTE SEMPRE >>>')
    
print('-='*30)

