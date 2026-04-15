S = [list(input().strip()) for _ in range(10)]

a, b, c, d = 0, 0, 0, 0

for i in range(10):
    for j in range(10):
        if S[i][j] == "#":
            if a == 0:
                a = i + 1
                c = j + 1
            if a != 0:
                b = i + 1
                d = j + 1

if b == 0:
    b = a
    c = d

print(a, b)
print(c, d)
