S = input()
ans = ""

for i in range(len(S)):
    if i != 0 and i != len(S):
        ans += "o"
    ans += S[i]

print(ans)
