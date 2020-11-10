
while True:
    print("-"*30)
    num = int( input("Quer ver a tabuada de qual valor? "))
    print("-"*30)
    if( num < 0):
        print("PROGRAMA TABUADA ENCERRAD0. volte sempre!")
        break
    for i in range(1, 11):
        print("{} x {:3} = {}".format(num,i,num*i))
    
