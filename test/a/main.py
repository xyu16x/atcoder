import sys


# 標準入力を高速化
def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]
    # for _ in range(N):
    #    s = list(input())
    #    S.append(s)

    for i in range(N):
        for j in range(N):
            if S[i][j] == "o":
                flg = False
                if i == 0:
                    for k in range(N):  # 列
                        if S[k][j] != "o":
                            break
                        if k == N - 1:
                            print("Yes_c")
                            exit()
                if j == 0:
                    for k in range(N):  # 行
                        if S[i][k] != "o":
                            break
                        if k == N - 1:
                            print("Yes_c")
                            exit()
                if (i == 0 and j == 0) or (i == 0 and j == N - 1):
                    for k in range(N):  # 左上から
                        if S[k][k] != "o":
                            break
                        if k == N - 1:
                            print("Yes_taihidari")
                            exit()
                    row = 0
                    col = N - 1
                    for _ in range(N):  # 右上から
                        print(row, col)
                        if S[row][col] != "o":
                            break
                        if row == N - 1:
                            print("Yes_taimigi")
                            exit()
                        row += 1
                        col -= 1

    print("No")


if __name__ == "__main__":
    main()
