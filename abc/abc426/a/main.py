import sys
import collections
import itertools
import math

# 再帰の上限を設定
sys.setrecursionlimit(10**7)


def _getId(s: str) -> int:
    if s == "Ocelot":
        return 1
    if s == "Serval":
        return 2
    if s == "Lynx":
        return 3
    else:
        return -1


# 標準入力を高速化
def main():
    # 入力
    S = input().split()

    x = _getId(S[0])
    y = _getId(S[1])

    if x >= y:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
