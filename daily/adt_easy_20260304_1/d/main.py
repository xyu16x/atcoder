a, b = map(int, input().split())

while a > 0 and b > 0:
    check_a = a % 10
    check_b = b % 10

    if (check_a + check_b) >= 10:
        print("Hard")
        exit()

    a //= 10
    b //= 10

print("Easy")
