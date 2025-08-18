N = int(input())
if N %2 == 0:
    print("No")
    exit()
S = list(input())
AS = S[:N//2]
mid = S[N//2]
BS = S[N//2 + 1:]
if AS.count('1') == N//2 and BS.count('2') == N//2 and mid == '/':
    print("Yes")
else:
    print("No")