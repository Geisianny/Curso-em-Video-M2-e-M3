print("x "*15)
print("10 TERMOS DE UMA PA")
print("x "*15)

num = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = num + (10 -1) * razao

for i in range(num,decimo,razao):   
    print(" {} - ".format(i), end='-> ')
print("ACABOU")
    
