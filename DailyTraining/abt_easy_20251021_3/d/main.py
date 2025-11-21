import sys


# 標準入力を高速化
def main():
    # 入力
    n = int(input())

    a = [list(input()) for _ in range(n)]
    b = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]:
                print(i + 1, j + 1)


if __name__ == "__main__":
    main()
