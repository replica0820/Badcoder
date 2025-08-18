while 1:
    n,m = map(int,input().split())
    ans = [0] * n
    if n == 0 and m==0:
        exit()
    for i in range(m):
        A = list(map(int,input().split()))
        ans = [x+y for (x,y) in zip(ans,A)]
    print(max(ans))