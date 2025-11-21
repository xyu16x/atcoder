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
    len_S = len(S)
    sitei = int((len(S) + 1) / 2)

    print(S[: sitei - 1] + S[sitei : len(S)])


if __name__ == "__main__":
    main()
