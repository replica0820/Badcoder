N,M = map(int,input().split())
check = [0]*N
S = list(input())
T = list(input())

for _ in range(M):
    L,R = map(int,input().split())
    check[L-1] -= 1
    check[R-1] += 1
    print(check)
now = 0
# for i in range(1,N):
#     check[i] = (check[i-1]+check[i])%2
# print(check)
# for i in range(N):
#     now = (now + check[i])%2
#     print(S[i] if now == 0 else T[i],end = '')