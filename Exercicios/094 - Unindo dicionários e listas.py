d = dict()
galera = list()
soma = 0
media = 0

while True:
    d.clear()
    d['Nome'] = str(input('Nome: '))
    while True:
        d['sexo'] = str(input('Sexo: [M/F]  '))
        if d['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.') 
    d['idade'] = int(input('Idade: '))
    soma += d['idade']
    galera.append(d.copy())
    while True:
        c = str(input('Quer continuar? [S/N] ')).upper()[0]
        if c in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if c == 'N':
        break
print('-='*30)
print('A) Ao todo temos {} pessoas cadastradas.'.format(len(galera)))
media = soma/len(galera)
print('B) A media de idade é de {:5.2f} anos.'.format(media))
print('C) As mulheres cadastradas forma', end='')
for p in galera:
    if p['sexo'] == 'F':
        print('{}'.format(p['Nome']), end='')
print()
print('D Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print('{} = {}; '.format(k,v), end='')
        print()
print('<<< encerrando >>>')
    
