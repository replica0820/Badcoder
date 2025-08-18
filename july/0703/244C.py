N = int(input())
print(1)
a = set(i+ 1 for i in range(1,2*N + 1))
while 1:
    n = int(input())
    if n == 0 or len(a) <= 1:
        exit()
    a.discard(n)
    print(a.pop())
