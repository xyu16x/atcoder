n = int(input())
a = list(map(int, input().split()))

ans = 1 + a[0]

for i in range(1, n):
    if i + 1 < ans:
        if i + 1 + a[i] > ans:
            ans = i + 1 + a[i]
        continue
    else:
        break

ans -= 1
if ans > n:
    ans = n
print(ans)
