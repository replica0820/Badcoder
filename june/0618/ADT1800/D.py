N = int(input())
count = 0
now = 1
while 1:
    double = 2** now
    if N % double == 0:
        count += 1
        now += 1
    else:
        print(count)
        exit()