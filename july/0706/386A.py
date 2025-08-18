A,B,C,D = map(int,input().split())
check = [0] * 13
check[A-1] += 1
check[B-1] += 1
check[C-1] += 1
check[D-1] += 1
two = 0
three = 0
for c in check:
    if c == 2:
        two += 1
    elif c == 3:
        three += 1
if two == 2 or three == 1:
    print("Yes")
else:
    print("No")