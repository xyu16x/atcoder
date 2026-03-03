s = list(input().split())

ans = []

if s[0] == "<":  # a<b
    ans.append("A")
    ans.append("B")
    if s[2] != "<":
        if s[1] == "<":
            ans.insert(1, "C")
        else:
            ans.insert(0, "C")

else:  # b<a
    ans.append("B")
    ans.append("A")

    if s[2] == ">":
        ans.insert(0, "C")
    else:
        if s[1] != "<":
            ans.insert(1, "C")

print(ans[1])
