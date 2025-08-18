from collections import defaultdict
Q = int(input())
ball = defaultdict(int)
check = set()
for _ in range(Q):
    querry = list(map(int,input().split()))
    if querry[0] == 1:
        ball[querry[1]] += 1
        if querry[1] not in check:
            check.add(querry[1])
    elif querry[0] == 2:
        ball[querry[1]] -= 1
        if ball[querry[1]] == 0:
            check.remove(querry[1])
    else:
        print(len(check))