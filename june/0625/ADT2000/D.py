N,M = map(int,input().split())
ans = 0
limit = 10**9
for i in range(M+1):
    ans += N**i
    if ans > limit:
        print("inf")
        exit()
print(ans)