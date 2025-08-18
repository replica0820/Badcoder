A = list(map(int,input().split()))
check = [0] * 13
for a in A:
    check[a-1] += 1
ans = sorted(check,reverse=True)
if ans[0] >= 3 and ans[1] >= 2:
    print("Yes")
else:
    print("No")