A = list(map(int,input().split()))
check = [0]*14
for a in A:
    check[a]+=1
new = sorted(check,reverse=True)
if new[0] >= 3 and new[1] >= 2:
    print("Yes")
else:
    print("No")