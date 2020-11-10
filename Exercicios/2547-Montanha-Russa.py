while True:
    try:
        n,m,ma = input().split()
        n = int(n)
        m = int(m)
        ma = int(ma)

        i = 0
        cont = 0
        while i < n:
            x = int(input())
            i += 1
            if m <= x and x <= ma:
                cont += 1
        print(cont)
    except EOFError:
      break
