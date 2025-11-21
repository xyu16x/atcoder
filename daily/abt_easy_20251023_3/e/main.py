import sys


# 標準入力を高速化
def main():
    n = int(input())
    a = list(map(int, input().split()))

    ini = 0
    now = 0

    for i in range(n):
        now += a[i]
        if ini + now < 0:
            ini = -now

    print(ini + now)


if __name__ == "__main__":
    main()
