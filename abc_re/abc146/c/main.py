import math

A, B, X = map(int, input().split())


# 整数Xを買うための金額
def f(x):
    return A * x + B * (int(math.log10(x)) + 1)


def search(target):
    left, right = 0, 10**9 + 1

    while left + 1 < right:
        mid = (left + right) // 2

        if f(mid) >= target:
            right = mid
        elif f(mid) <= target:
            left = mid

    return left


ans = search(X)

print(ans)
