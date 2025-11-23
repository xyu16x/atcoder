s = list(input())
ans = []

for i in range(len(s)):
    if s[i] != ".":
        ans.append(s[i])

print("".join(ans))
