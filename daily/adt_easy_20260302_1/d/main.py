s = list(input().strip())

d = 0
ans = 0

for i in range(len(s) - 2):
    if s[i] == "A":
        for j in range(i, len(s) - 1):
            if s[j] == "B":
                d = j - i
                for k in range(j, len(s)):
                    if s[k] == "C":
                        if k - j == d:
                            ans += 1

print(ans)
