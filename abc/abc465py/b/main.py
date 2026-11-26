X, Y, L, R, A, B = map(int, input().split())

ans = 0

if A < L and B < R:
    ans += (L - A) * Y
    ans += (R - B) * X
elif A < L and B > R:
    ans += (L - A) * Y
    ans += (R - L) * X
    ans += (B - R) * Y
elif A > L and R < B:
    ans += (R - A) * X
    ans += (B - R) * Y
elif A > L and R > B:
    ans += (B - A) * X

print(ans)
