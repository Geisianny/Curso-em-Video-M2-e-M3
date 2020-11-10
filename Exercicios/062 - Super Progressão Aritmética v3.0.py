print("Gerador de PA")
print("-=" * 10)
primeiro= int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

cont = 1
termo = primeiro
mais = 10
total = 0
while mais != 0:
    total = mais + total
    while(cont <= total):
        print("{} -> ".format(termo), end='')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos voce quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(total))
    
    
