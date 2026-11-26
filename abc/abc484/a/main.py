B, R = map(int, input().split())

grid = [[0] * 30 for _ in range(30)]

for _ in range(B):
    grid = grid[:-1]

for _ in range(R):
    grid = [row[:-1] for row in grid]

ans = sum(len(row) for row in grid)

print(ans)
