D = input()
ans = ['N','E','NE','NW','S','W','SW','SE']
print(ans[(ans.index(D)+4)%8])