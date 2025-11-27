x1, y1, x2, y2 = map(int, input().split())

dist5 = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

for d in dist5:
    x = x1 + d[0]
    y = y1 + d[1]

    distance = (x2 - x) ** 2 + (y2 - y) ** 2

    if distance == 5:
        print("Yes")
        exit()

print("No")
