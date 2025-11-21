n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
for i in range(n):
    if a[i] <= i + 1:
        print(a[i])
        exit()

else:
    print(0)
