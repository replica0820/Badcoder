Q = int(input())
now = 0
snake = []
next = 0
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        snake.append(next)
        next += q[1]
    elif q[0] == 2:
        now += 1
    else:
        print(snake[now+q[1]])
