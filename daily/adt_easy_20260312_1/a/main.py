S = list(input().strip())
ans = ""

for s in S:
    if s != "a" and s != "e" and s != "i" and s != "o" and s != "u":
        ans += s

print(ans)
