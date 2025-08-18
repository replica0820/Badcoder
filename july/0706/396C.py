N,M = map(int,input().split())
B = sorted(list(map(int,input().split())),reverse=True)
W = sorted(list(map(int,input().split())),reverse=True)

S,T,maxT=[0]*(N+1),[0]*(M+1),[0]*(M+1)
for i in range(N):
    S[i+1] = S[i] + B[i]

for i in range(M):
    T[i+1] = T[i] + W[i]
    maxT[i+1] = max(maxT[i],T[i+1])

ans = 0
for i in range(N+1):
    ans = max(ans,S[i]+maxT[min(i,M)])
print(ans)
