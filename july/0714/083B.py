N,A,B = map(int,input().split())
cnt = 0
for i in range(1,N+1):
    a = [int(x) for x in list(str(i))]
    if A <= sum(a) <= B:
        cnt += i
print(cnt)