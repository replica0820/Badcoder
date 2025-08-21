H = int(input())
day = 0
plant=0
while 1:
    if plant > H:
        print(day)
        exit()
    elif plant == H:
        print(day+1)
        exit()
    plant += 2**day

    day += 1