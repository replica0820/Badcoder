def base_n(num,n):
    count = 0
    while num:
        if num%n>=10:
            return -1
        count += num%n
        num //= n
    return count
T = int(input())
for i in range(T):
    N,K = map(int,input().split())
    count = base_n(N,3)
    if (count <= K and count%2 == K%2):
        print("Yes")
    else:
        print("No")

    