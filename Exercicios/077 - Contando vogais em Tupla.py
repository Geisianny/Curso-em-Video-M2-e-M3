palavras = ("APRENDER","PROGRAMAR","LINGUAGEM","PYTHON","CURSO",
            "GRÁTIS","ESTUDAR","PRATICAR","TRABALHAR","MERCADO","PROGRAMADOR","FUTURO")
for p in palavras:
    print("\nNa palavra {} temos ".format(p), end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=" ")
