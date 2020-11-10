entrada = int(input())
k = 0
total = 0.0
num = []
while k < entrada:
    cod,qnt = input().split(" ")
    cod = int(cod)
    qnt = int(qnt)
    k += 1
    
    if cod == 1001:
       total = 1.50 * qnt
    elif cod == 1002:
        total = (2.50*qnt)
    elif cod == 1003:
        total = (3.50*qnt)
    elif cod == 1004:
         total = (4.50*qnt)
    elif cod == 1005:
          total = (5.50 *qnt)
    num.append(total)
for i in range(len(num)):
    num[i] = float(num[i])
print("{:.2f}".format(sum(num)))
