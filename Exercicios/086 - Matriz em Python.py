matriz = [[0,0,0] ,[0,0,0],[0,0,0]]
for i in range(0,3):
    for k in range(0,3):
        matriz[i][k] = int(input("Digite um valor: [{},{}] ".format(i,k)))
      
print('-='*30)
for l in range(0,3):
    for k in range(0,3):
        print(f"[{matriz[l][k]}]", end='')
    print()
