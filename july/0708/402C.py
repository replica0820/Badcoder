N,M = map(int,input().split())
a = []
ans = [0] * N
for _ in range(M):
    K,*A = map(int,input().split())
    a.append(A)
B = list(map(int,input().split()))
order = {v: i for i, v in enumerate(B)}
print(order)
for AA in a:
    max_item = max(order[x] for x in AA)
    ans[max_item-1] += 1
cnt = 0
for i in range(N):
    cnt += ans[i]
    print(cnt)