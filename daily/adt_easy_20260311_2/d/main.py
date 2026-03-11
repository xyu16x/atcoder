x, k = map(int, input().split())

for i in range(1, k + 1):
    # print(i, 10**i, x)
    target = x % (10**i)
    x = x // (10**i)

    if target // (10 ** (i - 1)) >= 5:
        # print(target // (10 ** (i - 1)))
        x += 1

    x = x * (10**i)

    if x < 0:
        print(0)
        exit()

print(x)
