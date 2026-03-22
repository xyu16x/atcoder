from collections import deque

H, W = map(int, input().split())
S = [list(input().strip()) for _ in range(H)]

v = [[False] * W for _ in range(H)]

ans = 0

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "." and not v[i][j]:
            queue = deque()
            queue.append((i, j))
            v[i][j] = True
            check_border = False

            while queue:
                x, y = queue.popleft()

                if x == 0 or x == H - 1 or y == 0 or y == W - 1:  # 外周
                    check_border = True

                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < H and 0 <= ny < W:
                        if S[nx][ny] == "." and not v[nx][ny]:
                            v[nx][ny] = True
                            queue.append((nx, ny))

            if not check_border:
                ans += 1

print(ans)
