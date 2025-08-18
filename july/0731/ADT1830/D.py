S = list(input())
check = set()
Big_count = 0
small_count = 0
flag = 1
for s in S:
    if s in check:
        flag = 0
        break
    check.add(s)
    if ord(s) >= 97:
        small_count += 1
    else:
        Big_count+=1
if Big_count and small_count and flag:
    print("Yes")
else:
    print("No")

