from collections import deque

N, Q = map(int, input().split())
K = list(map(int, input().split()))

ans = deque(range(1, N + 1))

# print(N, Q, K, ans)

for k in K:
    lst = [ans.popleft() for _ in range(k)]
    ans.extendleft(-x for x in lst)

print(*ans, sep="\n")
