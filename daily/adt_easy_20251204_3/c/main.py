s = input()
cnt = 0
ans = []

for i in range(len(s)):
    if s[i] == "#":
        cnt += 1
        ans.append(i + 1)
        if cnt == 2:
            print(",".join(map(str, ans)))
            ans = []
            cnt = 0
    else:
        continue
