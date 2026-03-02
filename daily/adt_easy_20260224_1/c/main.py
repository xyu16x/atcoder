n = int(input())
s = [list(input()) for _ in range(n)]

wins = []

for i in range(len(s)):
    count = 0
    for j in range(n):
        if s[i][j] == "o":
            count += 1
    wins.append(count)

ans = []
for i in range(n - 1, -1, -1):
    for j in range(len(wins)):
        if i == wins[j]:
            ans.append(j + 1)

print(" ".join(map(str, ans)))
