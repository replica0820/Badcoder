S = list(input())
ans = []
for i in S:
    if ord(i) <= 90:
        new_s = chr(ord(i)+32)
        ans.append(new_s)
    else:
        ans.append(i)
print(*ans,sep = '')
