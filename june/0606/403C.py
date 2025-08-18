n,m,q = map(int,input().split())
see = [[0 for j in range(m)]for x in range(n)]
flag = [0] * n
for _ in range(q):
    s = list(map(int,input().split()))
    x = s[1] -1
    if s[0] == 1:
        see[x][s[2]-1]=1
    elif s[0] == 2:
        flag[x] = 1
    else:
        if see[x][s[2]-1] == 1 or flag[x] == 1:
            print("Yes")
        else:
            print("No")
