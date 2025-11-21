import sys
import collections
import itertools
import math

# 再帰の上限を設定
sys.setrecursionlimit(10**7)


# 標準入力を高速化
def main():
    # 入力
    n, m = map(int, input().split())
    a = [int(s) for s in input().split()]
    res = []

    if n - m == 0:
        print(0)
        print("")
        exit()

    for i in range(1, n + 1):
        res.append(i)

    for i in range(m):
        res.remove(a[i])

    print(n - m)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
