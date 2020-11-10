
def ajuda(com):
    help(com)

    
def titulo(msg):
    tam = len(msg) +4
    print('~'*tam)
    print(msg)
    print('~'*tam)

#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')
