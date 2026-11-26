N = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(N):
    if i < N // 2:
        continue
    else:
        ans += A[i]

print(ans)
