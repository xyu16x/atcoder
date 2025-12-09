n = int(input())
s = [input() for _ in range(n)]

status = "logout"
ans = 0

for i in range(n):
    if s[i] == "private":
        if status != "login":
            ans += 1
    elif s[i] == "login":
        status = s[i]
    elif s[i] == "logout":
        status = s[i]

print(ans)
