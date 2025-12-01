n = int(input())
x = list(map(int, input().split()))

total = 0
for i in range(n):
    total += x[i]

p = int(total / n + 0.5)

ans = 0

for i in range(n):
    ans += (x[i] - p) ** 2

print(ans)
