import sys


# 標準入力を高速化
def main():
    n, m, k = map(int, input().split())
    r_list = [list(input().split()) for _ in range(m)]

    key_num = []  # 使用した鍵の本数
    keys = []  # 使用した鍵
    res = []  # ox

    for r in r_list:
        key_num.append(int(r[0]))
        keys.append([r[index] for index in range(1, key_num[-1] + 1)])
        res.append(r[key_num[-1] + 1])


if __name__ == "__main__":
    main()
