n = int(input())
S = [input() for _ in range(n)]

ans = 0

for s in S:
    if s == "For":
        ans += 1

if n // 2 < ans:
    print("Yes")
else:
    print("No")
