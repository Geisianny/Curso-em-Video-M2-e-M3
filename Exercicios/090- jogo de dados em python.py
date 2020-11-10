d = {}
d['nome'] = str(input("Nome: "))
d['media'] = float(input("Media de {}: ".format(d['nome'])))
if d['media'] >= 7:
    d['situacao'] = 'aprovado'
elif 5 <=d['media'] < 7:
    d['situacao'] = 'recuperacao'
else:
    d['situacao'] = 'reprovado'
print('-='*30)
for k, v in d.items():
    print('{} é igual a {}'.format(k,v))
print('-='*30)


