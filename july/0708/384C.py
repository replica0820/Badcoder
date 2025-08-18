import itertools
a,b,c,d,e = map(int,input().split())
l = 'ABCDE'
member = set()

for r in range(1,len(l)+1):
    for x in itertools.combinations(l,r):
        member.add(x)
res = []
for m in member:
    cnt = 0
    if 'A' in m:
        cnt += a
    if 'B' in m:
        cnt += b
    if 'C' in m:
        cnt += c
    if 'D' in m:
        cnt += d
    if 'E' in m:
        cnt += e
    res.append((cnt,''.join(m)))
res.sort(key=lambda x: (-x[0],x[1]))
for i,j in res:
    print(j)