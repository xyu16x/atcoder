n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]
res = []

for i in range(n - m + 1):
    for j in range(n - m + 1):
        line = ""
        for col in range(m):
            for row in range(m):
                line += s[i + col][j + row]
        if line not in res:
            res.append(line)

print(len(res))
