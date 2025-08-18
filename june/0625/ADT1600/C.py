N = int(input())
A = []
for _ in range(N):
    a = list(input())
    A.append(a)
ans = []
for i in range(N):
    x = []
    for j in range(N):
        if i == 0 and j == 0:
            x.append(A[1][0])
        elif i == 0:
            x.append(A[i][j-1])
        elif i == N-1 and j == N-1:
            x.append(A[i-1][j])
        elif i == N-1:
            x.append(A[i][j+1])
        elif j == N-1:
            x.append(A[i-1][j])
        elif j == 0:
            x.append(A[i+1][j])
        else:
            x.append(A[i][j])
    ans.append(x)
for i in range(N):
    print(*ans[i],sep='')