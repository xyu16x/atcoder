import math

n, x, y = map(int, input().split())
a = list(map(int, input().split()))

c = y - x

a.sort()
w = a[0] * y
ans = a[0]

for i in range(1, n):
    wi = a[i] * y
    if (wi - w) % c != 0:
        print(-1)
        exit()

    n = (wi - w) // c
    if a[i] - n < 0:
        print(-1)
        exit()

    ans += a[i] - n

print(ans)
