num = int(input("Digite um numero para ver sua tabuada: "))
for i in range(1, 11):
   print("{} x {:2}  = {}".format(num, i, num*i))
