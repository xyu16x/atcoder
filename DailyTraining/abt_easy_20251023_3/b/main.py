import sys

# 再帰の上限を設定
sys.setrecursionlimit(10**7)


# 標準入力を高速化
def main():
    s = list(input())

    for i in range(len(s) - 1, -1, -1):
        if s[i] == "a":
            print(i + 1)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
