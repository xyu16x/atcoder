import sys


# 標準入力を高速化
def main():
    n = int(input())
    q = [list(map(int, input().split())) for _ in range(n)]
    ball = []

    for i in range(n):
        if len(q[i]) == 2:
            ball.append(q[i][1])
        if len(q[i]) == 1:
            m = min(ball)
            print(m)
            ball.remove(m)


if __name__ == "__main__":
    main()
