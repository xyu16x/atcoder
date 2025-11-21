import sys


# 標準入力を高速化
def main():
    l, r = map(int, input().split())
    s = "atcoder"

    print(s[l - 1 : r])


if __name__ == "__main__":
    main()
