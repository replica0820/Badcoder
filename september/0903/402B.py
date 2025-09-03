from collections import deque
Q = int(input())
matrix = deque()
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        matrix.append(query[1])
    else:
        print(matrix.popleft())
