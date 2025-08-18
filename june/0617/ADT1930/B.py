N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = []
for i in A:
    if i %K == 0:
        ans.append(i/K)
print(*ans)
