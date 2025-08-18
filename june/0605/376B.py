n,q = map(int,input().split())
count = 0
leftH = 1
rightH = 2
for _ in range(q):
    h,t = input().split()
    t = int(t)
    if h == 'L':
        ng = (rightH-leftH)%n
        to = (t-leftH)%n
        if ng < to:
            count += n-to
        else:
            count += to
        leftH = t
    else:
        ng = (leftH-rightH)%n
        to =(t - rightH)%n
        if ng < to:
            count += n-to
        else:
            count += to
        rightH = t
print(count)
