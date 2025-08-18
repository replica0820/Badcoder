N = int(input())
H = list(map(int,input().split()))
ans = [0] * N
ans[1] = abs(H[0] - H[1])
for i in range(2,N):
    ans[i] = min(ans[i-2]+ abs(H[i]-H[i-2]),ans[i-1]+abs(H[i]-H[i-1]))
print(ans[-1])
