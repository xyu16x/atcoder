n = int(input())
a = list(map(int, input().split()))

x = a[1] / a[0]
ans = a[0]

for i in range(1, n):
    if ans * x != a[i]:
        print("No")
        exit()
    else:
        if i != n - 1:
            ans = a[i]

else:
    print("Yes")
