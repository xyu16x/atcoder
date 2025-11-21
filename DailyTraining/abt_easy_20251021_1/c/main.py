import sys
import math


def main():
    n = int(input())
    x = [list(map(int, input().split())) for _ in range(n)]

    max = [0] * n
    index = [0] * n

    for i in range(n):
        for j in range(i, n):
            if i == j:
                l = 0
            else:
                l = math.sqrt((x[i][0] - x[j][0]) ** 2 + (x[i][1] - x[j][1]) ** 2)

            if max[i] < l:
                max[i] = l
                index[i] = j + 1
            if max[j] < l:
                max[j] = l
                index[j] = i + 1

        print(index[i])


if __name__ == "__main__":
    main()
