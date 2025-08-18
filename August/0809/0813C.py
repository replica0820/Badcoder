from collections import defaultdict
N,M = map(int,input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int,input().split()))
non = P[0]
P = P[1:]
ans = 0
FishDish = set()
Price = defaultdict(int)
for i in range(M):
    Price[D[i]] = P[i]
    FishDish.add(D[i])
for c in C:
    if c in FishDish:
        ans += Price[c]
    else:
        ans += non
print(ans)