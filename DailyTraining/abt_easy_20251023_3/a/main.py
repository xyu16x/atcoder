import sys


# 標準入力を高速化
def main():
    # 入力
    n = list(map(int, input().split()))
    s = []
    s.append(n[0])

    for i in range(1, len(n)):
        if n[i] not in s:
            s.append(n[i])

    print(len(s))


if __name__ == "__main__":
    main()
