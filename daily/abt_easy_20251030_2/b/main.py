s = input().split("-")
s1 = int(s[0])
s2 = int(s[1])


if s2 == 8:
    s1 += 1
    s2 = 1
else:
    s2 += 1

print(str(s1) + "-" + str(s2))
