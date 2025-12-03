s = input()

substring = set()


for i in range(len(s)):
    for j in range(i, len(s)):
        substring.add(s[i : j + 1])

ans = len(substring)
print(ans)
