N = int(input())

A = []

ans = [[] for _ in range(N)]

for i in range(N):
    a = list(map(int, input().split()))

    for j in range(1, a[0] + 1):
        ans[a[j] - 1].append(i + 1)


for a in ans:
    if len(a) == 0:
        print(len(a))
    else:
        print(len(a), " ".join(map(str, a)))
