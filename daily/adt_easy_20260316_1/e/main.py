def dfs(v, depth):
    if depth == N:
        return True
    for nxt in pair[v]:
        if not used[nxt]:
            used[nxt] = True
            if dfs(nxt, depth + 1):
                return True
            used[nxt] = False
    return False


N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

pair = [[] for _ in range(N)]


for i in range(N - 1):
    for j in range(i + 1, N):
        cnt = 0
        for k in range(M):
            if S[i][k] != S[j][k]:
                cnt += 1
            if cnt >= 2:
                break
            if k == M - 1:
                pair[i].append(j)
                pair[j].append(i)

# print(pair)

once = []

for i in range(M):
    target = i
    cnt = sum(row.count(target) for row in pair)

    if cnt == 0:
        print("No")
        exit()
    elif cnt == 1:
        once.append(i)

if len(once) >= 3:
    print("No")
    exit()

used = [False] * N

for start in range(N):
    used[start] = True
    if dfs(start, 1):
        print("Yes")
        exit()
    used[start] = False
print("No")
