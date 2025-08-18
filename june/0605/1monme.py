while True:
    N = int(input())
    if N == 0:
        break
    s = list(map(int,input().split()))
    x = sum(s)/N
    count = 0
    for j in range(N):
        if s[j] <= x:
            count += 1
    print(count)