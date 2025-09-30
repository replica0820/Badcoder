N,K = map(int,input().split())
A = set(map(int,input().split()))
person = []
light_person = []
for i in range(N):
    X,Y = map(int,input().split())
    if (i+1) in A:
        light_person.append((X,Y))
    else:
        person.append((X,Y))
max_dis = 0
for a,b in person:
    min_dis = -1
    for c,d in light_person:
        dis = ((a-c)**2 + (b-d)**2)
        if min_dis == -1:
            min_dis = dis
        else:
            min_dis = min(min_dis,dis)
    max_dis = max(max_dis,min_dis)
print(max_dis**(0.5))
    