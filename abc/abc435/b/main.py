n = int(input())
a = list(map(int, input().split()))

ans = []

for l in range(n):
    al_ar = a[l]
    for r in range(l + 1, n):
        al_ar += a[r]
        for k in range(l, r + 1):
            if al_ar % a[k] == 0:
                break
            elif k == r:
                ans.append(k)

print(len(ans))
