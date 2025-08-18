N,M = map(int,input().split())
A = []
B = []
Fib = [1,2]
start = int(input())
A.append(start)
B.append(start-1)
ans = 1
max_b = -1
for i in range(1,M):
    a = int(input())
    A.append(a)
    b = A[i] - A[i-1]
    max_b = max(max_b,b)
    if b == 1:
        print(0)
        exit()
    else:
        B.append(b)
if max_b >= 2:
    for j in range(2,max_b):
        Fib.append(Fib[j-2]+Fib[j-1])
        
for x in B:
    ans * Fib[x-1]
print(ans%1000000007)


