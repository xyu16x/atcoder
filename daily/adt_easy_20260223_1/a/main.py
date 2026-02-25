n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0

for b_i in b:
    ans += a[b_i - 1]

print(ans)
