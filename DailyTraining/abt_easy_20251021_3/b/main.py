import sys
import collections
import itertools
import math

# 再帰の上限を設定
sys.setrecursionlimit(10**7)


# 標準入力を高速化
def main():
    # 入力
    N, c1, c2 = input().split()
    S = list(input())

    for i in range(int(N)):
        if S[i] != c1:
            S[i] = c2

    print("".join(S))


if __name__ == "__main__":
    main()
