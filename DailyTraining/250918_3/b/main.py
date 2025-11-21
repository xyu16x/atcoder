import sys
import collections
import itertools
import math

# 標準入力を高速化
def main():
    # 入力
    n = int(input())

    if n <= 125:
        print(4)
    elif n <= 211:
        print(6)
    else:
        print(8)

if __name__ == "__main__":
    main()
