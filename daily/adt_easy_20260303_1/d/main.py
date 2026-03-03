n = int(input())
d = 0


if n <= 10**3 - 1:
    print(n)
elif n <= 10**4 - 1:
    d = n % 10
    print(n - d)
elif n <= 10**5 - 1:
    d = n % 100
    print(n - d)
elif n <= 10**6 - 1:
    d = n % 1000
    print(n - d)
elif n <= 10**7 - 1:
    d = n % 10000
    print(n - d)
elif n <= 10**8 - 1:
    d = n % 100000
    print(n - d)
else:
    d = n % 1000000
    print(n - d)
