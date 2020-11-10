print("="*30)
print("{:^30}".format("BANCO CEV"))
print("="*30)
valor = float(input("Que valor você quere sacar? R$"))
total = valor

totalced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print("Total de {} cédulas de R${}".format(totalced,ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total== 0:
            break
print("="*30)
print("Volte sempre ao BANCO CEV! tenha  um bom dia!")
