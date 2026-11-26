H, W = map(int, input().split())
C = [list(input().strip()) for _ in range(H)]

while C and all(cell == "." for cell in C[0]):
    C.pop(0)

while C and all(cell == "." for cell in C[-1]):
    C.pop()

while C and all(row[0] == "." for row in C):
    for row in C:
        row.pop(0)

while C and all(row[-1] == "." for row in C):
    for row in C:
        row.pop()

for c in C:
    print("".join(c))
