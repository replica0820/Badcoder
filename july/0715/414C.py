def decimal_to_base(n,base):
    if n==0:
        return '0'
    degits = []
    while n>0:
        re = n%base
        if re < 10:
            degits.append(str(re))
        else:
            degits.append(chr(ord('A')+re - 10))
        n //= base
    return ''.join(reversed(degits))

A = int(input())
N = int(input())
max = 10**6
ans = 0
for i in range(1,max):
    s = int(str(i) + str(i)[::-1])
    if s > N:
        continue
    k = ''
    check = decimal_to_base(s,A)
    if check == check[::-1]:
        ans += s
for i in range(1,max):
    s = int(str(i) + str(i)[:-1][::-1])
    if s > N:
        continue
    k = ''
    check = decimal_to_base(s,A)
    if check == check[::-1]:
        ans += s
print(ans)