X = int(input())
s = 1
i = 1
while 1:
    s *= i
    if s == X:
        print(i)
        break
    i += 1