n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort()

for i in range(n):
    ans = str(a[i][0]) + " " + str(a[i][1])
    print(ans)
