N,X = map(int,input().split())
A = list(map(int,input().split()))
ch = [0]*(N+1)
now = X
ch[X] = 1
while 1:
    next = A[now-1]
    if not ch[next]:
        ch[next] = 1
        now = next
    else:
        break
print(sum(ch))