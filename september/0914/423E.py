N,Q = map(int,input().split())
A = list(map(int,input().split()))

for _ in range(Q):
    ans = 0
    L,R = map(int,input().split())
    for i in range(L,R):
        m_cnt = R - i + 1
        l_cnt = i - L + 1
        cnt += A[i]*m_cnt*l_cnt
    print(ans)