N = int(input())
S = list(input())
T = list(input())
count = 0
for i in range(1,N+1):
    if S[-i:] == T[:i]:
        count = i
print(N*2-count)