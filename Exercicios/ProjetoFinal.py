def linha(tam = 42):
    return '-' * tam

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("ERRO: por favor, digite um número  inteiro válido.")
            continue
        except(KeyboardInterrupt):
            print("Usuario preferiu não digitar esse numero.")
            return 0
        else:
            return n
        
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print("{}- {}".format(c,item))
        c += 1
    print(linha())
    opc = leiaint("Sua opção: ")
    return opc
def arquivoexiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criararquivo(nome):
    try:
        a = open(nome, 'w')
        a.close()
    except:
        print("Houve um erro na criação do arquivo!")
    else:
        print("arquivo {} criado com sucesso!".format(nome))
def lerarquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace('\n', ' ')
            print("{:<30}{:>3} anos".format(dado[0],dado[1]))
    finally:
        a.close()
        
def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'a')
    except:
        print("Houve um erro na abertura do arquivo!")
    else:
        try:
            a.write("{};{}\n".format(nome,idade))
        except:
            print("Houve um erro na hora de escrever os dados!")
        else:
            print("Novo registro de {} adicionado".format(nome))
            a.close()
        

arq = "cursoemvideo.txt"
if not arquivoexiste(arq):
    criararquivo(arq)
             
while True:
    resposta = menu(["ver pessoas cadastradas", "Cadastrar nova Pessoas",  "Sair do Sistema"])
    if resposta == 1:
        #opção de listar o conteudo de um arquivo!
        lerarquivo(arq)
    elif resposta == 2:
         cabecalho("NOVO CADASTRO")
         nome = str(input("Nome: "))
         idade = leiaint("Idade: ")
         cadastrar(arq,nome,idade)
                   
    elif resposta == 3:
        cabecalho("Saindo do sistema ... Ate logo!")
        break
    else:
        print("ERRO! Digite uma opção valida!")
        
      


