N = int(input())
A = list(map(int,input().split()))
board = [0]*4
count = 0
for i in range(N):
    board[-1] += 1
    for _ in range(A[i]):
        board.append(0)
    count += sum(board[:A[i]])
    del board[:A[i]]
print(count)