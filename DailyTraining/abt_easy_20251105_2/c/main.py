h, w, n = map(int, input().split())

ans = [["." for _ in range(w)] for _ in range(h)]

now = [0, 0]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction_index = -1


for i in range(n):
    if ans[now[0]][now[1]] == ".":
        ans[now[0]][now[1]] = "#"
        direction_index = (direction_index + 1) % 4

    elif ans[now[0]][now[1]] == "#":
        ans[now[0]][now[1]] = "."
        direction_index = (direction_index + 1) % 4 if direction_index > 0 else 3

    now = [
        now[0] + direction[direction_index][0],
        now[1] + direction[direction_index][1],
    ]

    # for i in range(h):
    #    print("".join(ans[i]))

for i in range(h):
    print("".join(ans[i]))
