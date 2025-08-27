def nbtn(num):
    l = 0
    r = num
    while l < r:
        m = (l + r) // 2
        if check(m,X,K+1,N+1):
            l = m + 1
        else:
            r = m
    return l + 1

def check(border,slid,cnt,n):
    n_kan = 0
    count = 0
    for i in range(n):
        n_kan += slid[i]
        if n_kan >= border:
            n_kan = 0
            count += 1
    if count >= cnt:
        return 1
    else:
        return 0


N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split())) + [L]
X = [0]*(N+1)
X[0] = A[0]
for i in range(1,N+1):
    X[i] = A[i]-A[i-1]
ans = nbtn(L+1)
print(ans)

