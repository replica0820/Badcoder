N = int(input())
now = 0
cnt = 0
for i in range(N):
    S = input()
    if S == 'login':
        now = 1
    elif S == 'logout':
        now = 0
    elif S == 'private'and not now:
        cnt += 1
print(cnt)