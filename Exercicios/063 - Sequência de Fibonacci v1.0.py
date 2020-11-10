print("-"*40)
print("Sequencia de Fibonacci")
print("-"*40)
qnt = int(input("Quantos termos voce quer mostrar? "))

t1 = 0
t2 = 2
print("~"* 40)
print('{} -> {}'.format(t1,t2), end='')
c = 3
while(c <= qnt):
    t3 = t1 + t2
    print(" -> {}".format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(" -> FIM")
print("~"*40)    
