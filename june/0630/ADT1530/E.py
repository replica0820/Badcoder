N,M = map(int,input().split())
X = list(map(int,input().split()))
A = list(map(int,input().split()))
X.append(N-1)
s = sum(A)
if s != N or X[0] != 1:
    print(-1)
    exit()
stone = 0
ans = 0
for i in range(M):
    stone += A[i]
    ans += A[i] -1
    print(ans)
    if stone < X[i+1] - X[i]:
        print(-1)
        exit()
    else:
        stone -= (X[i+1]-X[i])
print(ans)