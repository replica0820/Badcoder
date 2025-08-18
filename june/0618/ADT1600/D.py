N,Q = map(int,input().split())
card = [0] * N
for _ in range(Q):
    event,num = map(int,input().split())
    if event == 1:
        card[num-1] += 1
    elif event == 2:
        card[num-1] += 2
    else:
        if card[num - 1] >= 2:
            print("Yes")
        else:
            print("No")