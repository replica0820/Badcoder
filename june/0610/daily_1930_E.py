N,Q = map(int,input().split())
parts = []
count = 0
head = []
for i in range(1,N+1):
    parts.append([i,0])
for j in range(Q):
    a,b = input().split()
    if int(a) == 1:
        if count == 0:
            if b == 'R':
                new_head = [parts[0][0]+1,parts[0][1]]
                head.append(new_head)
            elif b == 'L':
                new_head = [parts[0][0]-1,parts[0][1]]
                head.append(new_head)
            elif b == 'U':
                new_head = [parts[0][0],parts[0][1]+1]
                head.append(new_head)
            elif b == 'D':
                new_head = [parts[0][0],parts[0][1]-1]
                head.append(new_head)
        else:
            if b == 'R':
                new_head = [head[-1][0]+1,head[-1][1]]
                head.append(new_head)
            elif b == 'L':
                new_head = [head[-1][0]-1,head[-1][1]]
                head.append(new_head)
            elif b == 'U':
                new_head = [head[-1][0],head[-1][1]+1]
                head.append(new_head)
            elif b == 'D':
                new_head = [head[-1][0],head[-1][1]-1]
                head.append(new_head)
        count += 1

    else:
        if int(b)-count -1 < 0:
            y = abs(int(b)-count-1)
            print(*head[y-1])
        else:
            print(*parts[int(b)-count-1])
