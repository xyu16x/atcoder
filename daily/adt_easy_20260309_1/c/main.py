h, w, n = map(int, input().split())

# 現在いるマスが白である場合は現在のマスを黒にする
# 時計回りに90度回転、向いてる方向に1マス進む

# 現在いるマスが黒である場合は、現在のマスを白にする
# 反時計回りに90度回転して、向いている方向に1マス進む

cur_y, cur_x = 0, 0  # 高橋君が現在いるマス
directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 方向
dir_idx = 0  # 高橋君の方向

ans = [["."] * w for _ in range(h)]

for i in range(n):
    if ans[cur_y][cur_x] == ".":
        ans[cur_y][cur_x] = "#"
        dir_idx = (dir_idx + 1) % 4
        cur_x = (cur_x + directions[dir_idx][0]) % w
        cur_y = (cur_y + directions[dir_idx][1]) % h
    else:
        ans[cur_y][cur_x] = "."
        dir_idx = (dir_idx - 1 + 4) % 4
        cur_x = (cur_x + directions[dir_idx][0]) % w
        cur_y = (cur_y + directions[dir_idx][1]) % h

for i in range(len(ans)):
    print("".join(ans[i]))
