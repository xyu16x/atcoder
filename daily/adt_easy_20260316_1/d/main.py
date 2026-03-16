s = input()

ans = 0
flg = False

for i in range(len(s)):

    if flg:
        flg = False
        continue

    else:
        if s[i] == "0" and i != len(s) - 1:
            if s[i + 1] == "0":
                ans += 1
                flg = True
                continue
        else:
            ans += 1

print(ans)
