N,Q = map(int,input().split())
A = []
count = 0
for j in range(N):
    A.append(j+1)
for i in range(Q):
    query = list(map(int,input().split()))
    Q_type = query[0]
    p = query[1]
    if Q_type == 1:
        A[(p-1+count)%N] = query[2]
    elif Q_type == 2:
        print((p+count)%N)
        #print(A[(p-1+count)%N])
    else:
        count += p