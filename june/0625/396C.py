N,M = map(int,input().split())
B = sorted(list(map(int,input().split())),reverse=True)
W = sorted(list(map(int,input().split())),reverse=True)
b_ruiseki = [0]*(N+1)
w_ruiseki = [0]*(M+1)
maxT = [0]*(M+1)
for i in range(N):
    b_ruiseki[i+1] = b_ruiseki[i] + B[i]
for j in range(M):
    w_ruiseki[j+1] = w_ruiseki[j] + W[j]
    maxT[j+1] = max(maxT[j],w_ruiseki[j+1])

ans = 0
for i in range(N+1):
    ans = max(ans,b_ruiseki[i] + maxT[min(i,M)])
print(ans)