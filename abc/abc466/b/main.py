N, M = map(int, input().split())

k = [-1] * M

for _ in range(N):
    C, S = map(int, input().split())
    if k[C - 1] > 0 and k[C - 1] > S:
        continue
    else:
        k[C - 1] = S

print(" ".join(map(str, k)))
