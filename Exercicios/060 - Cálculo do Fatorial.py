#from math import factorial

num = int(input("Digite um numero: "))
#f = factorial(num)
    
#print("o fatorial do numero {} é {}".format(num,f))

#outraforma

c = num
f = 1
print("Calculando {}! = ".format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
