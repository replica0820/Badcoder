N = int(input())
A = set(map(int,input().split()))

for i in range(N+2):
    if i not in A:
        print(i)
        exit()