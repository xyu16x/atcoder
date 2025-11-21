import sys


# 標準入力を高速化
def main():
    # 入力
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    t = [list(input()) for _ in range(h)]

    for i in range(h):
        cs = 0
        ct = 0

        for j in range(w):
            if s[i][j] == "#":
                cs += 1
            if t[i][j] == "#":
                ct += 1

        if cs != ct:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
