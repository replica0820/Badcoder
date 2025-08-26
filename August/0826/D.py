S = list(input())
N = len(S)
for a in range(N+1):
    for b in range(N+1-a):
        c = N-a-b
        if list('A'*a + 'B'*b + 'C'*c) == S:
            print("Yes")
            exit()
print("No")