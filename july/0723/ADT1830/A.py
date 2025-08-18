N = int(input())
cnt = 0
judge = (N+1)//2
for _ in range(N):
    S = input()
    if S == 'For':
        cnt += 1
    if cnt >= judge:
        print("Yes")
        exit()
print("No")