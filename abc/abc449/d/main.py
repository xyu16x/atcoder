L, R, D, U = map(int, input().split())

ans = 0

# x, y -> max(|x|, |y|)
# 偶偶 -> 偶
# 奇奇 -> 奇

x = R - L + 1
y = U - D + 1
x_even = R // 2 - (L - 1) // 2
y_even = U // 2 - (D - 1) // 2
x_odd = x - x_even
y_odd = y - y_even

print(x, y, x_even, y_even)

# 偶偶
ans += x * y

# 偶奇 -> |x| > |y| の場合
start = L if L % 2 == 0 else L + 1
for i in range(start, R + 1, 2):
    lo = max(D, -(abs(i) - 1))
    hi = min(U, abs(i) - 1)
    if lo <= hi:
        ans += (hi - lo + 1) - (hi // 2 - (lo - 1) // 2)

# 奇偶 -> |x| < |y| の場合
start = D if D % 2 == 0 else D + 1
for i in range(start, U + 1, 2):
    lo = max(L, -(abs(i) - 1))
    hi = min(R, abs(i) - 1)
    if lo <= hi:
        ans += (hi - lo + 1) - (hi // 2 - (lo - 1) // 2)


print(ans)
