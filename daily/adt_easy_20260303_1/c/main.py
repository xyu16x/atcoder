def func(x):
    res = 0
    while x > 0:
        res += x % 10
        x = x // 10
    return res


n = int(input())
a = [1]
i = 1

while i < n:
    a.append(a[i - 1] + func(a[i - 1]))
    i += 1

print(a[n - 1])
