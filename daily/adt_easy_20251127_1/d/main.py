a, b, k = map(int, input().split())

cnt = a
ans = 0

while cnt < b:
    ans += 1
    cnt = cnt * k

print(ans)
