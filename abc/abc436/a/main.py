n = int(input())
s = input()

ans = []
for _ in range(n - len(s)):
    ans.append("o")

ans.append(s)

print("".join(ans))
