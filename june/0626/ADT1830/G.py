N,Q = map(int,input().split())
now = [[-1,-1] for _ in range(N)]
print(now)
for j in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        now[q[1]-1][1] = q[2]-1
        now[q[2]-1][0] = q[1]-1
    elif q[0] == 2:
        now[q[1]-1][1] = -1
        now[q[2]-1][0] = -1
    else:
        top = q[1]-1
        ans = []
        while now[top][0] != -1:
            top = now[top][0]
        ima = top
        ans.append(ima)
        while now[ima][1] != -1:
            ima = now[ima][1]
            ans.append(ima)
        print(*ans)