N,D = map(int,input().split())
cnt = 0
check = [0]*N
man = []
for i in range(N):
    X,Y = map(int,input().split())
    man.append((X,Y))
    check[i] = i+1