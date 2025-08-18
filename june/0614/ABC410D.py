# import heapq,math
# def dijkstra(N,list_Adj,start,goal):
#     dist = [math.inf]*N
#     dist[start] = 0
#     hq = []
#     heapq.heappush(hq,(0,start))
#     while hq:
#         cost,no = heapq.heappop(hq)
#         if dist[no]<cost:
#             continue
#         for g_no,g_cost in list_Adj[no]:
#             if dist[g_no]<=(dist[no]^g_cost):
#                 continue
#             dist[g_no] = dist[no]^g_cost
#             heapq.heappush(hq,(dist[g_no],g_no))
#     return dist[goal]
# N,M = map(int,input().split())
# edge = [[] for _ in range(N)]
# for i in range(M):
#     A,B,W = map(int,input().split())
#     edge[A-1].append((B-1,W))
# ans = dijkstra(N,edge,0,N-1)
# if ans == math.inf:
#   ans = -1
# print(ans)

from collections import deque

def xor_bfs(N, list_Adj, start, goal):
    max_xor = 1024  # 上限を必要に応じて調整（例：10ビット以内）
    visited = [False] * max_xor
    q = deque()
    q.append((start, 0))  # (現在のノード, 現在のXOR値)

    while q:
        node, val = q.popleft()
        if node == goal:
            return val
        for nxt, cost in list_Adj[node]:
            nxt_val = val ^ cost
            if not visited[nxt_val]:
                visited[nxt_val] = True
                q.append((nxt, nxt_val))
    return -1

N,M = map(int,input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    A,B,W = map(int,input().split())
    edge[A-1].append((B-1,W))
ans = xor_bfs(N,edge,0,N-1)
print(ans)
