s = input()
t = input()

if s == t:
    print(0)
else:
    limit = min(len(s), len(t))
    i = 0
    while i < limit:
        if s[i] != t[i]:
            print(i + 1)
            exit()
        i += 1
    print(limit + 1)
