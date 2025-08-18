N = int(input())
S = []
T = []
for _ in range(N):
    s = list(input())
    S.append(s)
for _ in range(N):
    t = list(input())
    T.append(t)
def sabun(A,B,X):
    count = 0
    for i in range(X):
        for j in range(X):
            if A[i][j] != B[i][j]:
                count += 1
    return(count)
def right_90(A):
    return list(zip(*S[::-1]))

ans = 10**9
for i in range(4):
    ans = min(ans,sabun(S,T,N)+i)
    S = right_90(S)

print(ans)
