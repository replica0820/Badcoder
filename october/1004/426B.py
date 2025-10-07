from collections import defaultdict
ans = defaultdict(int)
S = list(input())
check = set()
for s in S:
    ans[s] += 1
    check.add(s)
for x in check:
    if ans[x] == 1:
        print(x)
        exit()