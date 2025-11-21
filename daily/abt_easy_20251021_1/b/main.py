import sys


# 標準入力を高速化
def main():
    s, t, x = map(int, input().split())

    if t >= s:
        if s <= x and x < t:
            print("Yes")
            exit()
    else:
        if s <= x or x < t:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
