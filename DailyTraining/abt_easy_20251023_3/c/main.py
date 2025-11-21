import sys

# 再帰の上限を設定
sys.setrecursionlimit(10**7)


# 標準入力を高速化
def main():
    s = [list(input()) for _ in range(8)]
    row = []
    col = []

    for i in range(8):
        for j in range(8):
            if s[i][j] == "#":
                if i not in row:
                    row.append(i)
                if j not in col:
                    col.append(j)

    res = (8 - len(row)) * (8 - len(col))

    print(res)


if __name__ == "__main__":
    main()
