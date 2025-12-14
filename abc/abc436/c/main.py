n, m = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(m)]

ans = 0
kuro = set()

direct = [[0, 0], [0, 1], [1, 0], [1, 1]]

for i in range(m):
    kuro_kari = []
    br, bc = q[i]
    flg = True
    for dr, dc in direct:
        nr, nc = br + dr, bc + dc

        if not (1 <= nr <= n and 1 <= nc <= n):
            flg = False
            break

        if (nr, nc) in kuro:
            flg = False
            break

        kuro_kari.append((nr, nc))

    if flg:
        for k in kuro_kari:
            kuro.add(k)
        ans += 1

print(ans)
