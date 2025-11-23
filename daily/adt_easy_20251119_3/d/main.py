s = input()

ans = []

for i in range(0, len(s)):
    ans.append(s[i : len(s)] + s[0:i])

print(min(ans))
print(max(ans))
