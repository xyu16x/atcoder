n, m = map(int, input().split())
s = [list(map(int, input())) for _ in range(n)]

score = [0] * n

for i in range(m):
    zero = []
    one = []

    for j in range(n):
        if s[j][i] == 0:
            zero.append(j)
        else:
            one.append(j)

    if len(zero) == 0:
        for x in one:
            score[x] += 1
    elif len(one) == 0:
        for x in zero:
            score[x] += 1
    elif len(zero) > len(one):
        for x in one:
            score[x] += 1
    elif len(one) > len(zero):
        for x in zero:
            score[x] += 1

max = max(score)
ans = []


for i in range(len(score)):
    if score[i] == max:
        ans.append(i + 1)

print(" ".join(map(str, ans)))
