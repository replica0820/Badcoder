INF = 10 ** 16

def bellmanFordXOR(edges, vertex: int, start_node: int) -> list:
    # Initialize
    costs = [INF] * vertex
    costs[start_node] = 0
    for _ in range(vertex - 1):
        updated = False
        for f, t, c in edges:
            if costs[f] != INF and costs[t] > (costs[f] ^ c):
                costs[t] = costs[f] ^ c
                updated = True
        if not updated:
            break
    return costs

# 入力読み取り
N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B, W = map(int, input().split())
    edges.append((A - 1, B - 1, W))  # 0-indexed

# 実行
dist = bellmanFordXOR(edges, N, 0)
ans = dist[N - 1]
if ans == INF:
    ans = -1
print(ans)

