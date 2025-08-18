N = int(input())
count = 0
now_L = -1
now_R = -1
for _ in range(N):
    A,S = input().split()
    A = int(A)
    if S == 'L':
        if now_L == -1:
            now_L = A
        else:
            count+= abs(now_L-A)
    else:
        if now_R == -1:
            now_R = A
        else:
            count+= abs(now_R - A)
    print(count)
print(count)
    