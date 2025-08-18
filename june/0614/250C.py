N,Q = map(int,input().split())
val=[]
pos=[]
for i in range(N):
    val.append(i)
    pos.append(i)
for j in range(Q):
    v = int(input()) - 1
    p = pos[v]
    if p != N-1:
        p2 = p + 1
    else:
        p2 = p - 1
    v2 = val[p2]
    val[p],val[p2] = val[p2],val[p]
    pos[v],pos[v2] = pos[v2],pos[v]

print(*val)