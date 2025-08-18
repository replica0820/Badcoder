K = int(input())
t = K // 60
m = K % 60
t += 21 % 24
ans = []
ans.extend(str(t))
ans.extend(':')
if m < 10:
    ans.extend('0')
ans.extend(str(m))
print(*ans,sep='')