S = input()

ans = []

for s in S:
    if s.isdigit():
        ans.append(s)

print("".join(ans))
