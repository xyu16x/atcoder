h, w, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [int(input()) for _ in range(n)]

ans = 0

for i in range(h):
    cnt = 0
    for j in range(len(b)):
        cnt += a[i].count(b[j])
    if ans < cnt:
        ans = cnt

print(ans)
