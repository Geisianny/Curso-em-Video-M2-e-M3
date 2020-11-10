di = dict()
partidas = list()
total = 0
di['nome'] = str(input("Nome do Jogador: "))
vezes = int(input('Quantas partidas {} jogou? '.format(di['nome'])))
for i in range(0,vezes):
    partidas.append( int(input("Quantos gols na partida {}: ".format(i))))
for i in partidas:
    total += int(i)
di['partidas'] = partidas[:]
di['total'] = total
print('-='*30)
print(di)
print('-='*30)
for k, v in di.items():
    print('O campo {} tem o valor {}'.format(k,v))
print('-='*30)
print('O jogador {} jogou {} partidas.'.format(di['nome'],len(di['partidas'])))
for i,v in enumerate(di['partidas']):
    print('     => Na partida {}, fez {} gols.'.format(i,v))
