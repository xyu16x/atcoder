import sys


# 標準入力を高速化
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0

    for i in range(n):
        sum += a[i]

    for i in range(n):
        if sum - a[i] == m:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
