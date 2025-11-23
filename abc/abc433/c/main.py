import math

s = list(map(int, input()))

ans = 0
cntx = 1
cnty = 0
x = s[0]
y = 0

for i in range(1, len(s)):
    if x == s[i] and cnty == 0:
        cntx += 1
    else:
        if y == 0:
            y = s[i]
            if (x + 1) == y:
                cnty += 1
            else:
                x = s[i]
                cntx = 1
                y = 0
                cnty = 0
        elif y == s[i]:
            cnty += 1
            if cntx <= cnty:
                ans += min(cntx, cnty)
                x = y
                cntx = cnty
                y = 0
                cnty = 0
            else:
                continue
        else:
            ans += min(cntx, cnty)
            if s[i] == (y + 1):
                x = y
                cntx = cnty
                y = s[i]
                cnty = 1
            else:
                x = s[i]
                cntx = 1
                y = 0
                cnty = 0

ans += min(cntx, cnty)
print(ans)
