N = int(input())
clear = set()
for i in range(2,2*N + 2):
    clear.add(i)
print(1)
while 1:
    a = int(input())
    clear.remove(a)
    if len(clear) == 0:
        exit()
    res = list(clear)
    b = res[0]
    print(b)
    clear.remove(b)
    if len(clear) == 0:
        exit()
    