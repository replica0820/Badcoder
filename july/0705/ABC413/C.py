Q = int(input())
A = []
cnt = []
now = 0
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        A.append(q[2])
        cnt.append(q[1])
    if q[0] == 2:
        check = 0
        suum = 0
        aa = 0
        while 1:
            if check + cnt[now] >= q[1]:
                aa = q[1] - check
                suum += A[now] * aa
                cnt[now] -= aa
            else:
                suum += A[now] * cnt[now]
                check += cnt[now]
                now += 1
        print(sum)
print(A,cnt)