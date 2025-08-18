N = int(input())
S = list(input())
len_s = len(S)
ans = [0]*3
for i in range(len_s):
    if S[i] == 'A':
        ans[0] = 1
    elif S[i] == 'B':
        ans[1] = 1
    else:
        ans[2] = 1
    if sum(ans) == 3:
        print(i+1)
        exit()

