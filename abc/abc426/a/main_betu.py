import sys
import collections
import itertools
import math

# 再帰の上限を設定
sys.setrecursionlimit(10**7)


def _getId(s: str) -> int:
    if s == "Ocelot":
        1
    if s == "Serval":
        2
    if s == "Lynx":
        3
    else:
        -1


# 標準入力を高速化
def main():
    # 入力
    S = input().split()

    dict = {"Ocelot": 1, "Serval": 2, "Lynx": 3}

    if dict[str(S[0])] >= dict[str(S[1])]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
