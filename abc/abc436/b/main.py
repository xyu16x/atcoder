n = int(input())

ans = [[0] * n for _ in range(n)]

r = 0
c = (n - 1) // 2
k = 1

ans[r][c] = k

while k < n**2:
    next_r = (r - 1) % n
    next_c = (c + 1) % n
    k += 1

    if ans[next_r][next_c] == 0:
        r, c = next_r, next_c
    else:
        r = (r + 1) % n

    ans[r][c] = k


for row in ans:
    print(*row)
