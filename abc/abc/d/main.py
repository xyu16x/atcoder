import bisect

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_A = []
current_sum = 0

A.sort()

for i in range(n):
    current_sum += A[i]
    sum_A.append(current_sum)

# print(A, sum_A)

ans = 0

for b in B:
    idx = bisect.bisect_left(A, b)
    # print(idx)

    small = 0 if idx == 0 else (b * idx - sum_A[idx - 1])
    large = 0 if idx == n else sum_A[n - 1] - sum_A[idx] + A[idx] - b * (n - idx)

    # print(small, large)

    ans += small + large

print(ans % 998244353)
