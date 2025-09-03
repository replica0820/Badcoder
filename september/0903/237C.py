S = list(input())
N = len(S)
flag = 1
cnt1 = 0
cnt2 = 0
for i in range(N):
    if S[i] != 'a':
        flag = 0
        break
    else:
        cnt1 += 1
for j in range(N-1,0,-1):
    if S[j] != 'a':
        break
    else:
        cnt2 +=1
x = cnt2-cnt1
T = ['a']*x + S
if flag or (T == T[::-1] and cnt1 <= cnt2):
    print("Yes")
else:
    print("No")