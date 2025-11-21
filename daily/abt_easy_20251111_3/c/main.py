n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

max = 0
ans = 0

max_sub = r[0]
ans_sub = 1

i = 0
while i < n:
    if c[i] == t:
        if max < r[i]:
            ans = i + 1
            max = r[i]
    if c[i] == c[0]:
        if max_sub < r[i]:
            ans_sub = i + 1
            max_sub = r[i]

    i += 1

if max == 0 and ans == 0:
    print(ans_sub)
else:
    print(ans)
