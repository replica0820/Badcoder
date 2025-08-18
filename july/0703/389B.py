X = int(input())
ans = 1
i = 1
while 1:
    ans *= i
    if ans == X:
        print(i)
        break
    i += 1