S = list(map(int,input()))
x = len(S)
i = 0
cnt = 0
flag = 1
for i in range(x):
    cnt += 1
    if S[i] == 0 and S[i-1] == 0:
        if flag:
            cnt -= 1
            flag = 0
        else:
            flag = 1
    else:
        flag = 1
print(cnt)
