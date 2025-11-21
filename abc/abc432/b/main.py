x = list(map(int, input()))
x.sort()

ans = []
i = 0

while i < len(x):
    if x[i] != 0:
        ans.append(x[i])
        if i != 0:
            ans = ans = ans + [0] * i
        ans = ans + x[i + 1 :]
        break

    i += 1


print("".join(map(str, ans)))
