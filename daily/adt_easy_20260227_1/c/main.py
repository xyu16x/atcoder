a_list = list(map(int, input().split()))

ans = 0

for i, a in enumerate(a_list):
    if a != 0:
        ans += 2**i * a

print(ans)
