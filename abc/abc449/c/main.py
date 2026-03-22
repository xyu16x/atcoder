import bisect

N, L, R = map(int, input().split())
S = list(input().strip())

ans = 0

pos = [[] for _ in range(26)]

for idx, ch in enumerate(S):
    pos[ord(ch) - 97].append(idx)

# print(pos)

for p in pos:
    for i in range(len(p)):
        l = p[i] + L
        r = p[i] + R
        l = bisect.bisect_left(p, l)
        h = bisect.bisect_right(p, r)
        ans += h - l


print(ans)
