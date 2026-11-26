N = int(input())
C = list(map(int, input().split()))

colors = [0 for _ in range(N)]

for c in C:
    colors[c - 1] += 1

m = max(colors)

# print(m)

print(len(C) - m)
