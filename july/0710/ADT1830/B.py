S = list(input())
c = ''.join(S[:3])
n = ''.join(S[3:])
if c == 'ABC':
    if 1 <= int(n) <= 315 or 317 <= int(n) <= 349:
        print("Yes")
        exit()
print("No")