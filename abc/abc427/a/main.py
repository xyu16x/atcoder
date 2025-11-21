import sys
import collections
import itertools
import math

# 再帰の上限を設定
sys.setrecursionlimit(10**7)


# 標準入力を高速化
def main():
    # 入力
    S = input()
    l = len(S)
    sitei = int((l + 1) / 2)

    S = S[: sitei - 1] + S[sitei:l]

    print(S)


if __name__ == "__main__":
    main()
