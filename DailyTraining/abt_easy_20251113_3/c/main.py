n = int(input())

ans = []


for i in range(n):
    line = []
    for j in range(i + 1):
        if j == 0 or j == i:
            line.append(1)
        else:
            line.append(ans[i - 1][j - 1] + ans[i - 1][j])
    ans.append(line)

for i in range(len(ans)):
    print(" ".join(map(str, ans[i])))
