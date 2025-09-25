N = int(input())
ans = ['-'] * N
ok = N//2 - 1
ans[ok+1] = '='
if N%2 == 0:
    ans[ok]='='
print(*ans,sep='')