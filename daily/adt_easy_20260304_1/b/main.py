a, b = map(int, input().split())

if a != b:
    for i in range(1, 4):
        if i != a and i != b:
            print(i)
else:
    print(-1)
