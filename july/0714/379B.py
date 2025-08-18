N,K = map(int,input().split())
S = list(input().split('X'))
ans = 0
for s in S:
    ans += len(s)//K
print(ans)