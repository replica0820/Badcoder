Q = int(input())
snake = []
head = []
top = 0
tyousei = 0
for i in range(Q):
    q = list(map(int,input()))
    if q[0] == 1:
        snake.append(q[1])
        count += 1
        if len(snake) == 1:
            head.append(0)
        else:
            head.append(head(-1)+snake(-1))
    elif q[0] == 2:
        tyouse += snake[top]
        top+=1
    else:
        print(head[q[1]]+tyousei)

        

