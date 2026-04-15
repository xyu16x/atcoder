from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input().strip()) for _ in range(R)]

ans = 0

visited = [[False] * C for _ in range(R)]
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

queue = deque()
queue.append([sy - 1, sx - 1, 0])

while queue:
    y, x, cnt = queue.popleft()
    visited[y][x] = True

    for dx, dy in dirs:
        ny, nx = y + dy, x + dx

        if 0 <= ny <= R - 1 and 0 <= nx <= C - 1:
            if c[ny][nx] == "." and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append([ny, nx, cnt + 1])

                if nx == gx - 1 and ny == gy - 1:
                    print(cnt + 1)
                    exit()
