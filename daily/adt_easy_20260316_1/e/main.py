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

print(pair)

once = []
