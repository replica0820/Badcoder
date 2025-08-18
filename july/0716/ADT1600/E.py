from collections import defaultdict
N = int(input())
Q = int(input())
box = [[] for _ in range(N+1)]
card = defaultdict(set)
for _ in range(Q):
    qu = list(map(int,input().split()))
    if qu[0] == 1:
        i,j = qu[1],qu[2]
        box[j].append(i)
        card[i].add(j)
    elif qu[0] == 2:
        i = qu[1]
        print(*sorted(box[i]))
    else:
        i = qu[1]
        print(*sorted(card[i]))