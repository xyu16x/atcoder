s = input()
t = input()

ans = 0
index_s = []
index_t = []
chars_s = []
chars_t = []

count = 0
for char in s:
    if char != "A":
        chars_s.append(char)
        index_s.append(count)
        count = 0
    else:
        count += 1

index_s.append(count)

count = 0
for char in t:
    if char != "A":
        chars_t.append(char)
        index_t.append(count)
        count = 0
    else:
        count += 1

index_t.append(count)

if chars_s != chars_t:
    print(-1)
else:
    ans = 0
    for i in range(len(index_s)):
        ans += abs(index_s[i] - index_t[i])
    print(ans)
