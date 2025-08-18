N = int(input())
ans = []
for _ in range(N):
    x = input()
    if x == '-----':
        ans.append(0)
    elif x == '.----':
        ans.append(1)
    elif x == '..---':
        ans.append(2)
    elif x == '...--':
        ans.append(3)
    elif x == '....-':
        ans.append(4)
    elif x == '.....':
        ans.append(5)
    elif x == '-....':
        ans.append(6)
    elif x == '--...':
        ans.append(7)
    elif x == '---..':
        ans.append(8)
    elif x == '----.':
        ans.append(9)

print(*ans,sep = '')
