N,M,K = map(int,input().split())
cnt = [0] * (N+1)
ans = []
for _ in range(K):
    A,B = map(int,input().split())
    cnt[A] += 1
    if cnt[A] == M:
        ans.append(A)
print(*ans,sep=' ')