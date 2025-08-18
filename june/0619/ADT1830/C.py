N,M = map(int,input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int,input().split()))
money = 0
for i in range(N):
    flag = 1
    for j in range(M):
        if C[i] == D[j]:
            flag = 0
            money += P[j+1]
    if flag:
        money += P[0]
print(money)