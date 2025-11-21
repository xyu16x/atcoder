n = int(input())
t = input()

direct = [[1, 0], [0, -1], [-1, 0], [0, 1]]
current = [0, 0]
x = 0

for i in range(n):
    if t[i] == "S":
        current[0] += direct[x][0]
        current[1] += direct[x][1]
    elif t[i] == "R":
        x += 1
        x = x % 4

print(" ".join(map(str, current)))
