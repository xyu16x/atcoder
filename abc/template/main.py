import sys
import collections
import itertools
import math

# 標準入力を高速化
def main():
    # 入力
    S, A, B, X = map(int, input().split())
    time = 0
    res = 0

    while(time <= X):
        if (A <= X - time):
            res += S * A
            time += A
        else:
            res += S * (X-time)
            print(res)
            exit()
        if (B <= X - time):
            time += B
        else:
            print(res)
            exit()


if __name__ == "__main__":
    main()
