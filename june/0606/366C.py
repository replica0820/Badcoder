from collections import defaultdict
Q = int(input())
d = defaultdict(int)
for _ in range(Q):
    querry = list(map(int,input().split()))
    if querry[0] == 1:
        d[querry[1]] += 1
    elif querry[0] == 2:
        d[querry[1]] -= 1
        if d[querry[1]] == 0:
            del d[querry[1]]
    else:
        x = len(d)
        print(x)
        
