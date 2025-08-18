while 1:
    n,m,t,p = map(int,input().split())
    sum = 0
    if n==0 and m ==0 and t==0 and p==0:
        break
    ansx = [1] * n
    ansy = [1] * m
    for _ in range(t):
        d,c = map(int,input().split())
        if d == 1:
            for j in range(c):
                if 2 * c >= len(ansx):
                    for _ in range(2*c-len(ansx)):
                        ansx.append(0)
                ansx[2*c-1-j] += ansx[j]
            del ansx[:c]
        else:
            for i in range(c):
                if 2*c >= len(ansy):
                    for _ in range(2*c-len(ansy)):
                            ansy.append(0)
                ansy[2*c-1-i] += ansy[i]
            del ansy[:c]
    for _ in range(p):
        x,y = map(int,input().split())
        print(ansx[x]*ansy[y])