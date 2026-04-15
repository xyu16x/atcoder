T, X = map(int, input().split())
A = list(map(int, input().split()))

t = A[0]
print(0, t)

for i in range(1, T + 1):
    # print(i, t, A[i])
    if abs(A[i] - t) >= X:
        t = A[i]
        print(i, t)
