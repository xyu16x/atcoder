n = int(input())
h = list(map(int, input().split()))

one = h[0]

for i in range(1, n):
    if one < h[i]:
        print(i + 1)
        exit()
else:
    print(-1)
