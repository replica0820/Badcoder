s = list(input())
t = list(input())
n = len(s)
count = 0

for x in range(n):
    if s[x]!= t[x]:
        count+=1
print(count)
for i in range(n):
    s_ord = ord(s[i])
    t_ord = ord(t[i])
    if s_ord > t_ord:
        s[i] = t[i]
        ans = ''.join(s)
        print(ans)
    
for j in reversed(range(n)):
    if s[j] != t[j]:
        s[j] = t[j]
        ans = ''.join(s)
        print(ans)