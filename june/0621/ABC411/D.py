N,Q = map(int,input().split())
PC = [[] for _ in range(N)]
server = []
for i in range(Q):
    q = list(input().split())
    p = int(q[1])
    if int(q[0]) == 1:
        PC[p-1].clear()
        PC[p-1].extend(server)
    elif int(q[0]) == 2:
        PC[p-1].extend(q[2])
    else:
        server.clear()
        server.extend(PC[p-1])
print(*server,sep='')