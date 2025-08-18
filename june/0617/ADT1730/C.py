from collections import defaultdict
N = int(input())
d = defaultdict(str)
name = set()
for i in range(N):
    S = input()
    name.add(S)
    if S in d:
        d[S] += 1
    else:
        d[S] = 1
print(max(d,key=d.get))
