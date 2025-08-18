# N = int(input())
# A = list(map(int,input().split()))
# ch = 10**5 + 1
# book = [0] * ch
# cnt = 0
# for j in range(N):
#     a = A[j]
#     if a >= ch:
#         memo = j-1
#         cnt+=1
#     else:
#         book[a-1] += 1
# ans = 0
# for i in range(ch):
#     if not book[i]:
#         if cnt >= 2:
#             cnt -=2
#             book[i] = 1
#             ans += 1
#         elif cnt == 1:
#             cnt = 0
#             if i >= A[memo]:
#                 ans += 1
#                 print(ans)
#                 exit()
#             else:
#                 book[A[memo]] = 0
#                 memo -= 1
#         else:
#             memo -= 1
#             if i >= A[memo]:
                
