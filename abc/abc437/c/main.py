t = int(input())

for _ in range(t):
    n = int(input())
    rein = [list(map(int, input().split())) for _ in range(n)]  # w, p

    cost = []
    p = 0

    for i in range(n):
        cost.append(rein[i][0] + rein[i][1])
        p += rein[i][1]

    cost.sort()

    ans = 0
    c_sum = 0

    for c in cost:
        if c_sum + c <= p:
            c_sum += c
            ans += 1
        else:
            break

    print(ans)
