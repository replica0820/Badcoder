N = int(input())
D = list(map(int,input().split()))
for i in range(N-1):
    dis = 0
    ans = []
    for j in range(i,N-1):
        dis += D[j]
        ans.append(dis)
    print(*ans)
