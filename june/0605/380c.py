n,k = map(int,input().split())
s = list(input())
count = 0
now = -1
ans = []
escape = []
check = 1
for i in range(n):
    if s[i] == '1':
        ans.append(1)
        if now == -1 or now == 0:
            now = 1
            count += 1

    else:
        if count == k-1:
            escape.append(0)
        elif count == k and now == 1:
            ans.append(0)
            ans.extend(escape)
            check = 0
        else:
            ans.append(0)
        now = 0
if check:
    ans.extend(escape)
print(*ans,sep='')
    
