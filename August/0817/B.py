from collections import defaultdict
ball = defaultdict(int)
balls = set()
Q = int(input())
min_list = 101
for _ in range(Q):
    A = list(map(int,input().split()))
    if A[0] == 1:
        if A[1] in balls:
            ball[A[1]] += 1
        else:
            ball[A[1]] = 1
            balls.add(A[1])
    else:
        x = min(balls)
        print(x)
        ball[x] -= 1
        if ball[x] == 0:
            balls.remove(x)