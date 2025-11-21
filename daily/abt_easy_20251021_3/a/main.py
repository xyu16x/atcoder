import sys
import collections
import itertools
import math

# 再帰の上限を設定
sys.setrecursionlimit(10**7)


# 標準入力を高速化
def main():
    # 入力
    N = int(input())
    S = input()
    flg_a = False
    flg_b = False

    for i in range(N):
        if flg_a:
            if S[i] == "b":
                print("Yes")
                exit()
        if flg_b:
            if S[i] == "a":
                print("Yes")
                exit()

        if S[i] == "a":
            flg_a = True
        elif S[i] == "b":
            flg_b = True
        else:
            flg_a = False
            flg_b = False

    print("No")


if __name__ == "__main__":
    main()
