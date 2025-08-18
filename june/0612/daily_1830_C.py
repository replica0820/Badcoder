N = int(input())
ans = []
for i in range(N):
    gyo = []
    for j in range(N):
        a = N-1-i
        b = i
        c = N-1-j
        d = j
        x = min(a,b,c,d)
        if x%2 == 0:
            gyo.append('#')
        else:
            gyo.append('.')
    ans.append(gyo)
for y in range(N):
    print(*ans[y],sep='')