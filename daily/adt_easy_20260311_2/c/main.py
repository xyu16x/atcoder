s = input()

n = len(s)
chars = []

for i in range(n):
    for j in range(i + 1, n + 1):
        chars.append(s[i:j])

ans = set(chars)

print(len(ans))
