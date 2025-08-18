from collections import defaultdict
neko = defaultdict(int)
N,K = map(int,input().split())
count = set()
for i in range(N):
    a,b = map(int,input().split())
    count.add(a)
    neko[a] += b
new_set = sorted(count)
ans = 0
for a in new_set:
    ans += neko[a]
    if ans >= K:
        print(a)
        break