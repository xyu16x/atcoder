n = int(input())
x = list(map(int, input().split()))

r = []
r.append(0)
min_list = []
min_list.append(x[0])


for i in range(n):
    r.append(x[i])
    ans = 0
    min = 0
    for j in range(len(r)):
        if j == i + 1:
            min_list.append(min)
        else:
            new_min = abs(r[j] - x[i])
            if j == 0:
                min = new_min
            if min_list[j] > new_min:
                min_list[j] = new_min
            if min > new_min:
                min = new_min
        ans += min_list[j]
    print(ans)
