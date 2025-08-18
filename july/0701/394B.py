N = int(input())
ans = []
a = []
for i in range(N):
    s = input()
    a.append([len(s),s])
res = sorted(a)
for x in range(N):
    ans.append(res[x][1])
print(*ans,sep='')