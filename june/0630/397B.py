S = list(input())
cnt = 0
a = len(S)
for i in range(a):
    if (i+cnt+1) %2 == 1 and S[i] == 'o':
        cnt += 1
    elif (i+cnt+1)%2 == 0 and S[i] =='i':
        cnt += 1
if (cnt + a) %2 == 1:
    cnt += 1
print(cnt)