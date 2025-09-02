K,G,M = map(int,input().split())
grass = 0
mag = 0
for _ in range(K):
    if grass == G:
        grass = 0
    elif mag == 0:
        mag = M
    else:
        sa = min(G-grass,mag)        
        grass += sa
        mag -= sa
print(grass,mag)