import sys
import collections
import itertools
import math

# 標準入力を高速化
def main():
    # 入力
    n = int(input())
    p = list(map(int, input().split()))

    r = 1
    res = [0] * n
    
    for i in range(n):
        k = 0
        max_p = max(p)
        for i, x in enumerate(p):
            if x == max_p:
                res[i] = r
                p[i] = 0
                k += 1
        r += k
        if r > n:
            break
    
    for re in res:
        print(re)


if __name__ == "__main__":
    main()
