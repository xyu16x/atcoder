N = int(input())
A = list(map(int, input().split()))

ans = 0

A.sort()

flg = False
for i in range(len(A)):
    if i < len(A) - 1:
        if not flg and A[i] == A[i + 1]:
            flg = True
        elif not flg:
            ans += A[i]
        else:
            flg = False
    else:
        if not flg:
            ans += A[i]

print(ans)
