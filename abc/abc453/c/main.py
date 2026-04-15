N = int(input())
L = list(map(int, input().split()))

cur = 0.5
ans = 0

for i in range(N):
    if cur > 0:
        cur -= L[i]
        if cur < 0:
            ans += 1
    else:
        cur += L[i]
        if cur > 0:
            ans += 1

print(ans)
