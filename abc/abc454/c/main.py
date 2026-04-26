from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

visited = [False] * (N + 1)

queue = deque([1])
visited[1] = True

while queue:
    v = queue.popleft()
    for nv in G[v]:
        if not visited[nv]:
            visited[nv] = True
            queue.append(nv)

print(sum(visited))
