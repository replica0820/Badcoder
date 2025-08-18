N = int(input())
cnt = 0
ans = []
for _ in range(N):
    c,l = input().split()
    l = int(l)
    cnt += l
    if cnt > 100:
        print("Too Long")
        exit()
    for _ in range(l):
        ans.append(c)
print(*ans,sep='')