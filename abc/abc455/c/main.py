from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
sum = 0

cnt = {}
for x in A:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1
    sum += x

vals = []
for x, c in cnt.items():
    vals.append(c * x)

vals.sort(reverse=True)

for i in range(K):
    sum -= vals[i]
    if sum == 0:
        break

print(sum)
