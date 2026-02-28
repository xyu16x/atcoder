h, m = map(int, input().split())

h1 = h // 10
h2 = h % 10

m1 = m // 10
m2 = m % 10

if h2 > 5 or h2 == 5 and m1 > 3:
    h2 = 0
    if h1 == 2:
        h1 = 0
    elif h1 == 1:
        h1 = 2
        if m1 > 3:
            m1 = 0
            m2 = 0
    else:
        h1 = 1

elif m1 > 3:
    m1 = 0
    m2 = 0

    if h2 == 9:
        h2 = 0
        h1 += 1
        h1 = h1 % 3
    else:
        h2 += 1


h = h1 * 10 + h2
m = m1 * 10 + m2

print(h, m)
