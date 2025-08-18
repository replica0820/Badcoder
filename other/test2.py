n = int(input())
count = 0
i = 1
while 2**i <= n:
    x = 2**i
    low = 0
    high = n // x
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n // x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    count += (ans + 1) // 2

    i += 1

print(count)
