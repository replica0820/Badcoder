N = int(input())
A = list(map(int,input().split()))
now = -1
cnt = 0
for a in A:
    if now == a:
        cnt += 1
    else:
        cnt = 1
        now = a
    if cnt == 3:
        print("Yes")
        exit()
print("No")