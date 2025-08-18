N,K = map(int,input().split())
H = list(map(int,input().split()))
ans = [10**9] * N
ans[0] = 0
ans[1] = abs(H[1]-H[0])
now = 2
while now < N:
    i = 1
    while i <= K and now - i >= 0:
        if ans[now] > ans[now-i]+abs(H[now]-H[now-i]):
            ans[now] = ans[now-i]+abs(H[now]-H[now-i])
        i+=1
    now+=1
print(ans[-1])
