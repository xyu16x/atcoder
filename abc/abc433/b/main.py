n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if i == 0:
        print(-1)
    else:
        for j in range(i - 1, -1, -1):
            if a[i] < a[j]:
                print(j + 1)
                break
            if j == 0:
                print(-1)
