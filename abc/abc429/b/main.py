x = int(input())
n = int(input())
w = list(map(int, input().split()))
q = int(input())
p = [int(input()) for _ in range(q)]

ans = x
buhin = []

for i in range(q):
    if p[i] not in buhin:
        ans += w[p[i] - 1]
        buhin.append(p[i])
    else:
        buhin.remove(p[i])
        ans -= w[p[i] - 1]
    print(ans)
