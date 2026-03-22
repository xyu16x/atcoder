n = int(input())
ans = []

for i in range(n, 0, -1):
    ans.append(i)

print(",".join(map(str, ans)))
