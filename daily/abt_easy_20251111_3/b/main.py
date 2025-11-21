a, b, c, d, e, f, x = map(int, input().split())

len_t = 0
len_a = 0

lap = 0
amari = 0

lap = x // (a + c)
amari = x % (a + c)

if amari >= a:
    len_t = a * b * (lap + 1)
else:
    len_t = a * b * lap + amari * b


lap = x // (d + f)
amari = x % (d + f)

if amari >= d:
    len_a = d * e * (lap + 1)
else:
    len_a = d * e * lap + amari * e

if len_t > len_a:
    print("Takahashi")
elif len_t == len_a:
    print("Draw")
else:
    print("Aoki")
