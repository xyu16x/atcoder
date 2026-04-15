N = int(input())
S = input()

ans = ""
flg = True

for s in S:
    if s != "o":
        flg = False
        ans += s
    elif s == "o" and not flg:
        ans += s

print(ans)
