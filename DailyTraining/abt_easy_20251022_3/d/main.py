import sys


# 標準入力を高速化
def main():
    # 入力
    N, D = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, D + 1):
        max = 0
        for j in range(len(t)):
            weight = t[j][0] * (t[j][1] + i)
            if weight > max:
                max = weight
        print(max)


if __name__ == "__main__":
    main()
