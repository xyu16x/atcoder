n = int(input())
t = list(map(int, input().split()))

ans = []

for i in range(3):
    min_t = min(t)
    idx = t.index(min_t)
    t[idx] = 200

    ans.append(idx + 1)

print(" ".join(map(str, ans)))
