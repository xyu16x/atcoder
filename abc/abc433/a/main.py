x, y, z = map(int, input().split())

n = x - (z * y)
d = z - 1

if n < 0:
    print("No")
    exit()

if n % d == 0:
    print("Yes")
else:
    print("No")
