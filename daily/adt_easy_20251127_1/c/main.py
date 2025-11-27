a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_b = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
b_c = (c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2
c_a = (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2

if a_b + b_c == c_a:
    print("Yes")
    exit()
elif a_b + c_a == b_c:
    print("Yes")
    exit()
elif b_c + c_a == a_b:
    print("Yes")
    exit()
else:
    print("No")


# a_b = [b[0] - a[0], b[1] - a[1]]
# a_c = [c[0] - a[0], c[1] - a[1]]
#
# if a_b * a_c == 0:
#    print("Yes")
#    exit()
#
# b_a = [-a_b[0], -a_b[1]]
# b_c = [c[0] - b[0], c[1] - b[1]]
#
# if b_a * b_c == 0:
#    print("Yes")
#    exit()
#
# c_a = [-a_c[0], -a_c[1]]
# c_b = [-b_c[0], -b_c[1]]
