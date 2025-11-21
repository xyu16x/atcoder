import sys
import collections
import itertools
import math

# 標準入力を高速化
def main():
    # 入力
    n = int(input())
    s = list(input())

    # ここにコードを書いてください
    if n % 2 != 1:
        print("No")
        exit()
    
    x = (n+1)/2

    for i in range(n):
        if n > 1 and i <= x - 2:
            if s[i] != "1":
                print("No")
                exit()
        elif i == x - 1:
            if s[i] != "/":
                print("No")
                exit()
        else:
            if s[i] != "2":
                print("No")
                exit()

    # 出力
    print("Yes")

if __name__ == "__main__":
    main()
