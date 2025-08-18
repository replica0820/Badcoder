n,m = map(int,input().split())
s = set()

for _ in range(m):
    a,b = map(int,input().split())
    s.add((a,b))
    for x in [-1,1]:
        for y in[-2,2]:
            s.add((a+x,b+y))
            s.add((a+y,b+x))

ans= n*n
for i,j in s:
    if 1<=i<=n and 1<=j<=n:
        ans-=1
print(ans)