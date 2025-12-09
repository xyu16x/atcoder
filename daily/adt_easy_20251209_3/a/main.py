M, D = map(int, input().split())
y, m, d = map(int, input().split())
ans = [0] * 3

ans[0] = y
ans[1] = m
ans[2] = d + 1

if ans[2] > D:
    ans[2] -= D
    ans[1] += 1
if ans[1] > M:
    ans[1] -= M
    ans[0] += 1

print(" ".join(map(str, ans)))
