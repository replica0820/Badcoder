N,K,X = map(int,input().split())
A = list(map(int,input().split()))
ans = A[:K]
ans.append(X)
ans.extend(A[K:])
print(*ans)