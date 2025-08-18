R,C = map(int,input().split())
new_R = min(16-R,R)
new_C = min(16-C,C)
ans = min(new_C,new_R)
if ans%2 == 1:
    print("black")
else:
    print("white")
