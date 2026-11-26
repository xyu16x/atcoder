import sys
from collections import defaultdict

data = sys.stdin.read().split()
idx = 0
N = int(data[idx])
idx += 1
M = int(data[idx])
idx += 1

A = [0] * M
B = [0] * M
for i in range(M):
    A[i] = int(data[idx])
    idx += 1
    B[i] = int(data[idx])
    idx += 1

cnt = [0] * (N + 1)
for a in A:
    cnt[a] += 1

shift = defaultdict(lambda: defaultdict(int))
for a, b in zip(A, B):
    shift[a][b] += 1


order = sorted(range(1, N + 1), key=lambda c: (-cnt[c], c))
rank1, rank2 = order[0], order[1]

out = []
for k in range(1, N + 1):
    base = rank1 if rank1 != k else rank2
    candidates = {base: cnt[base]}

    for c, add in shift.get(k, {}).items():
        candidates[c] = cnt[c] + add

    best_val = max(candidates.values())
    best_idx = min(c for c, v in candidates.items() if v == best_val)
    out.append(best_idx)

print("\n".join(map(str, out)))
