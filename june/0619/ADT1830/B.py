N = int(input())
ans = ['L']
for i in range(N):
    ans.append('o')
ans.extend(['n','g'])
print(*ans,sep = '')