S = list(input())
count = 0
for i in range(1,len(S)+1):
    if (i+count)%2 == 1 and S[i-1] == 'o':
        count += 1
    elif (i+count)%2 == 0 and S[i-1] == 'i':
        count += 1
if (count+i)%2 == 1:
    count +=1
print(count)