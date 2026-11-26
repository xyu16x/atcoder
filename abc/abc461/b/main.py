N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if i + 1 == B[A[i] - 1]:
        cnt += 1

if cnt == N:
    print("Yes")
else:
    print("No")
