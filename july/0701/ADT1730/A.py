N,M = map(int,input().split())
S = list(input())
T = list(input())
check = T[:N]
ketu = T[M-N:]
flag = 0
if S == check:
    flag = 1
if S == ketu:
    if flag:
        print(0)
    else:
        print(2)
else:
    if flag:
        print(1)
    else:
        print(3)