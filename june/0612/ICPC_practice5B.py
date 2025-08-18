while 1:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        exit()
    key_board = []
    for _ in range(h):
        A = list(map(int,input().split()))
        key_board.append(A)
    in_put = list(input())
    x = len(in_put)
    b4h = 0
    b4w = 0
    count = 0
    for i in range(x):
        for H in range(h):
            for W in range(W):
                if key_board[h][w] == in_put[i]:
                    count += abs(b4h - h) + abs(b4w-w)
    print(count)