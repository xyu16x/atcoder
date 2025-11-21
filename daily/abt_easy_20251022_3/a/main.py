import sys


# 標準入力を高速化
def main():
    # 入力
    x, y = map(int, input().split("."))

    if 0 <= y and y <= 2:
        print(str(x) + "-")
    elif 3 <= y and y <= 6:
        print(x)
    else:
        print(str(x) + "+")


if __name__ == "__main__":
    main()
