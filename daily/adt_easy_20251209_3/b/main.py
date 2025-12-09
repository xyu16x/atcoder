a, b = map(int, input().split())

x = 0
ans = 2

if a == b:
    print(1)
    exit()
else:
    # a,x,b/ b,x,a
    if (b - a) % 2 == 0:
        ans += 1

print(ans)
