N,Q = map(int,input().split())
box = [1] * (N+1)
box[0] = 0
poppo = [i for i in range(1,N+2)]
cnt = 0
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        box[poppo[q[1]]] -= 1
        if box[poppo[q[1]]] == 1:
            cnt -= 1
        box[q[2]] += 1
        if box[q[2]] == 2:
            cnt += 1
        poppo[q[1]] = q[2]
    else:
        print(cnt)