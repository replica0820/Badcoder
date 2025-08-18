arr = []
T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(N,0,-1):
        if bin_count(i) == 3:
            print(i)
            break
    print(-1)
