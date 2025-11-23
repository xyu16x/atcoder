n = int(input())
d = list(map(int, input().split()))


for i in range(n - 1):
    ans = []
    total = 0
    for j in range(i, n - 1):
        total += d[j]
        ans.append(total)
    print(" ".join(map(str, ans)))
