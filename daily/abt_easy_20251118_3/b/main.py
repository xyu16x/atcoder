a = list(map(int, input().split()))

x = a[0]
y = 0
x_cnt = 1
y_cnt = 0

for i in range(1, 5):
    if x == a[i]:
        x_cnt += 1
    elif y == a[i]:
        y_cnt += 1
    elif y == 0:
        y = a[i]
        y_cnt += 1

if x_cnt == 3 and y_cnt == 2:
    print("Yes")
elif x_cnt == 2 and y_cnt == 3:
    print("Yes")
else:
    print("No")
