import sys


# 尺取り法
def main():
    n, m, c = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    dict = {}

    for i in range(n):
        dict[a[i]] = dict.get(a[i], 0) + 1

    arr = []
    for k, v in dict.items():
        arr.append([k, v])
    arr = sorted(arr)

    for i in range(len(arr) - 1):
        arr[i + 1][1] += arr[i][1]
    for i in range(len(arr)):
        arr.append([arr[i][0] + m, arr[i][1] + n])

    result, j = 0, 0
    for i in range(len(dict)):
        while arr[j][1] - arr[i][1] < c:
            j += 1
        result += (arr[j][1] - arr[i][1]) * (arr[i + 1][0] - arr[i][0])
    print(result)


if __name__ == "__main__":
    main()
