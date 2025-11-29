n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = [0] * m
cnt = [0] * m

for i in range(n):
    ans[a[i][0] - 1] = ans[a[i][0] - 1] + a[i][1]
    cnt[a[i][0] - 1] = cnt[a[i][0] - 1] + 1

for i in range(m):
    ans[i] = round(ans[i] / cnt[i], 6)
    print("{:.20f}".format(ans[i]))
