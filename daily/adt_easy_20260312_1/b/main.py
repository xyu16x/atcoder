N, C = map(int, input().split())
T = list(map(int, input().split()))

tp = 0
ans = 0

for t in T:
    if tp == 0 or t - tp >= C:
        ans += 1
        tp = t

print(ans)
