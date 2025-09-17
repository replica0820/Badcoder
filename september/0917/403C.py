from collections import defaultdict
N,M,Q = map(int,input().split())
page = defaultdict(set)
full = [0] * (N+1)
for _ in range(Q):
    qu = list(map(int,input().split()))
    if qu[0] == 1:
        page[qu[1]].add(qu[2])
    elif qu[0] == 2:
        full[qu[1]] = 1
    else:
        if full[qu[1]] or qu[2] in page[qu[1]]:
            print("Yes")
        else:
            print("No")