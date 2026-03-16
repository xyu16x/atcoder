N = int(input())

ans = ""

for i in range(N):
    c, l = input().split()
    l = int(l)

    if l > 100:
        print("Too Long")
        exit()

    for j in range(l):
        ans += c

    if len(ans) > 100:
        print("Too Long")
        exit()

print(ans)
