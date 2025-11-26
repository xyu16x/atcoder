n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(k)]

correct = [0] * n

ans = []

for i in range(k):
    ppl = a[i][0]
    correct[ppl - 1] += 1
    if correct[ppl - 1] == m:
        ans.append(ppl)

print(" ".join(map(str, ans)))
