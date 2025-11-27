x, y, n = map(int, input().split())

# 1個あたり
y_one = y / 3

if y_one < x:
    y_cnt = n // 3
    x_cnt = n - y_cnt * 3
    print(x_cnt * x + y_cnt * y)
else:
    print(n * x)
