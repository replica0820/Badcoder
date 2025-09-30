N,M = map(int,input().split())
person = 2*N
score = [0] * person
hito = [x for x in range(person)]
rank = [x for x in range(person)]
hand = []
for _ in range(person):
    A = list(input())
    hand.append(A)

for i in range(M):
    for j in range(N):
        a = hand[rank[2*j]][i]
        b = hand[rank[2*j+1]][i]
        if (a == 'G' and b == 'C') or (a == 'C' and b == 'P') or (a == 'P' and b == 'G'):
            score[rank[2*j]] += 1
        elif a == b:
            score[rank[2*j]] += 0
        else:
            score[rank[2*j+1]] += 1
    rank = [h for _, h in sorted(zip(score, hito), key=lambda x: x[0], reverse=True)]
for r in rank:
    print(r+1)