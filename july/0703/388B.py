N,D = map(int,input().split())
hutosa = []
heavy = []
for i in range(N):
    T,L = map(int,input().split())
    now = T*L
    hutosa.append(T)
    heavy.append(now)
for j in range(1,D+1):
    heavy_hebi = 0
    for x in range(N):
        heavy_hebi = max(heavy_hebi,heavy[x]+(hutosa[x]*j))
    print(heavy_hebi)