n = int(input())
s = list(input())
ans = []

for i in range(n):
    if s[i] == "n":
        if i != n - 1 and s[i + 1] == "a":
            ans.append("nya")
        else:
            ans.append(s[i])
    elif s[i] == "a":
        if i != 0 and s[i - 1] == "n":
            continue
        else:
            ans.append(s[i])
    else:
        ans.append(s[i])

print("".join(ans))
