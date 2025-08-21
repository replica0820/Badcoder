S = list(input())
big_count = 0
small_count = 0
small = []
big = []
for s in S:
    small.append(s.lower())
    big.append(s.upper())
    if 97 <= ord(s) <= 122:
        small_count += 1
    else:
        big_count += 1
if small_count < big_count:
    print(*big,sep='')
else:
    print(*small,sep='')