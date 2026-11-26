import heapq

N, K, M = map(int, input().split())

V = []

for i in range(N):
    c, v = map(int, input().split())
    V.append((c, v))

V = sorted(V, key=lambda x: x[1], reverse=True)

chioce_c = set()
zan = []
ans = 0
cnt = 0

for i, (c, v) in enumerate(V):
    if c not in chioce_c:
        chioce_c.add(c)
        ans += v
    else:
        zan.append(v)

    if len(chioce_c) == M:
        index = i
        break

for i in range(K - M + 1):
    if len(zan) >= i:
        ans += zan[i]
    else:
        ans += V[index + i]

print(ans)
