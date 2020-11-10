matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for k in range(0,3):
        matriz[i][k]= int(input("Digite o valor de [{}][{}] ".format(i,k)))

print("-="*30)
soma = 0
soma3 = 0
maior = 0
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    print()
print('-='*30)
print('A soma dos numeros pares é: {}'.format(soma))
for l in range(0,3):
    soma3 += matriz[l][2]
print("A soma dos valores da terceira coluna é {}".format(soma3))
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print("O maior valor da segunda linha: {} ".format(maior))
