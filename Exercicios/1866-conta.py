entrada = int(input())

k = 0
while(k< entrada):
    num = int(input())
    k += 1
    soma = 0
    for i in range(0,num):
        if( i%2 == 0):
            soma += 1
        elif ( i% 2 != 0):
            soma = soma - 1
    print(soma)
