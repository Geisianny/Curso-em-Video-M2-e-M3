p1 = int(input("primeiro segmento: "))
p2 = int(input("segundo segmento: "))
p3 = int(input("terceiro segmento: "))

if( p1 < p2 + p3 and p2 < p3 + p1 and p3 < p2 + p1):
    print("PODEM FORMAR um triangulo", end = '')
    if(p1 == p2 == p3):
        print(" EQUILÁTERO")
    elif( p1 == p2 or p1 == p3 or p3== p2):
        print(" ISÓSCELES")
    else:
        print(" ESCALENO")
else:
    print("NÃO PODE FORMAR um triangulo")
