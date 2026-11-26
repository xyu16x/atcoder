import sys
import math


def main():
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    count = [0] * n

    for i in range(n):
        count[a[i] - 1] += 1

    # for i in range(n):
    #    if count[i] >= 2:
    #        res += math.comb(count[i], 2) * (n - count[i])

    for c in count:
        if c >= 2:
            res += int(c * (c - 1) / 2 * (n - c))

    print(res)


if __name__ == "__main__":
    main()
