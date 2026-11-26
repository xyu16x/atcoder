N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

p, s = 0, 0

for i in range(N):
    if A[i] != B[i]:
        break
    else:
        p += 1

for i in range(N - 1, -1, -1):
    if A[i] != B[i]:
        break
    else:
        s += 1

if p == N:
    print("Yes")
    exit()

a = A[p : N - s]
b = B[p : N - s]

if a[0] == b[-1] and a[1:] == b[:-1]:
    print("Yes")
elif a[-1] == b[0] and a[:-1] == b[1:]:
    print("Yes")
else:
    print("No")
