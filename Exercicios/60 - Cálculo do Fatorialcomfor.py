num = int(input("Digite um numero : "))

f = 1
for i in range(num, 0, -1):
    print("{}".format(i), end='')
    print(" x " if i > 1 else ' = ', end='')
    f *= i
print("{}".format(f))
