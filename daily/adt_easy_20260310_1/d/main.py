A, M, L, R = map(int, input().split())  # A基点, Mmおき, L:takahashi, R:aoki


lk = (L - A + M - 1) // M
rk = (R - A) // M

print(rk - lk + 1)
