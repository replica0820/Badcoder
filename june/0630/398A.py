N = int(input())
if N % 2 == 1:
    ans = ['-'] * (N -1)
    ans.insert((N-1)//2,'=')
else:
    ans = ['-'] * (N-2)
    ans.insert((N-2)//2,'==')
print(*ans,sep='')
