N, H, M = map(int, input().split())
now = set()
now.add((H, M))
count = 0

for _ in range(N):
    A, B = map(int, input().split())
    next_set = set()
    if len(now) == 0:
        break
    for h, m in now:
        if h >= A:
            next_set.add((h - A, B))
        if m >= B:
            next_set.add((h, m - B))
    now = next_set
    count += 1

print(len(now))
