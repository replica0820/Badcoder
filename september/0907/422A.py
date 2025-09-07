i,j = map(int,input().split('-'))
ans = [0,'-',0]
if j < 8:
    ans[0] = i
    ans[2] = j+1
elif i < 8 and j == 8:
    ans[0] = i + 1
    ans[2] = 1
print(*ans,sep = '')