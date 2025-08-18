N = int(input())
S = input()
if N %2 == 1:
    S_bef = S[:N//2]
    S_aft = S[N//2+1:]
    if '2' in S_bef or '/' in S_bef or '1' in S_aft or '/' in S_aft or S[N//2] != '/':
        print("No")
    else:
        print("Yes")
else:
    print("No")