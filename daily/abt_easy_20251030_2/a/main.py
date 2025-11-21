n, k, a = map(int, input().split())

ans = (k + a) % n
if ans == 0:
    print(n)
else:
    print(ans - 1)
