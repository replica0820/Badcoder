N,M,Q = map(int,input().split())
check = set()
flag = [0] * N
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        check.add((q[1],q[2]))
    elif q[0] == 2:
        flag[q[1]-1] = 1
    else:
        if flag[q[1]-1] or (q[1],q[2]) in check:
            print("Yes")
        else:
            print("No")