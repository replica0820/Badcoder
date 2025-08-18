while 1:
    d,w = map(int,input().split())
    if d ==0 and w ==0:
        exit()
    grid = []
    for _ in range(d):
        S = list(map(int,input().split()))

        grid.append(S)