H, W = map(int, input().split())

ans = [["." for _ in range(W)] for _ in range(H)]


for i in range(H):
    for j in range(W):
        if i == 0:
            ans[i][j] = "#"
        if i == H - 1:
            ans[i][j] = "#"
        if j == 0:
            ans[i][j] = "#"
        if j == W - 1:
            ans[i][j] = "#"

for i in range(H):
    print("".join(ans[i]))
