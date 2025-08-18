N,K = map(int,input().split())
ans = []
for _ in range(K):
    S = input()
    ans.append(S)
print(*sorted(ans))
    