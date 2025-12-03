n, m = map(int, input().split())
s = [list(map(int, input())) for _ in range(n)]

score = [0] * n
res = [0] * m

for i in range(m):
    zero = []
    one = []
    for j in range(n):
        if s[j][i] == 0:
            zero.append(j)
        else:
            one.append(j)
    if len(zero) < len(one) or len(zero) == n:
        for k in range(len(zero)):
            score[zero[k]] += 1
    else:
        for k in range(len(one)):
            score[one[k]] += 1

max = max(score)
ans = []

for i in range(n):
    if score[i] == max:
        ans.append(i + 1)

print(" ".join(map(str, ans)))
