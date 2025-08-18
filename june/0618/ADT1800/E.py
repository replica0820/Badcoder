N,Q = map(int,input().split())
two_poppo = set()
poppo = []
poppo_count = [1]*N
for i in range(N+1):
    poppo.append(i)
print(poppo)
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        before = poppo[q[1]]
        after = q[2]
        poppo_count[before] -= 1
        if poppo_count[before] == 1:
            two_poppo.remove(before)
        poppo_count[after] += 1
        if poppo_count[after] >= 2:
            two_poppo.add(after)
        poppo[before] = after
    else:
        print(two_poppo)
