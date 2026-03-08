n, m = map(int, input().split())
c = list(map(int, input().split()))  # コショウの残り
a = [list(map(int, input().split())) for _ in range(n)]
# a[i][0] 料理にかけられるコショウの種類
# a[i][1] 料理にかけられる故障の上限

ans = 0

for i in range(n):
    if c[a[i][0] - 1] - a[i][1] > 0:
        ans += a[i][1]
        c[a[i][0] - 1] -= a[i][1]
    else:
        ans += c[a[i][0] - 1]
        c[a[i][0] - 1] = 0

print(ans)
