import sys

# 再帰の上限を設定
sys.setrecursionlimit(10**7)


# 標準入力を高速化
def main():
    # 入力
    n = list(map(int, input().split()))

    print((n[0] + n[1]) * (n[2] - n[3]))
    print("Takahashi")


if __name__ == "__main__":
    main()
