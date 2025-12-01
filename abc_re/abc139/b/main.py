a, b = map(int, input().split())

ans = 0
current = 1

if (b - 1) % (a - 1) == 0:
    ans = (b - 1) // (a - 1)
else:
    ans = (b - 1) // (a - 1) + 1

print(ans)
