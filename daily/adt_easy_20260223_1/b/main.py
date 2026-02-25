n = list(map(int, input().strip()))

count_one = 0
count_two = 0
count_three = 0

for i in n:
    if i == 1:
        count_one += 1
    elif i == 2:
        count_two += 1
    elif i == 3:
        count_three += 1

if count_one == 1 and count_two == 2 and count_three == 3:
    print("Yes")
else:
    print("No")
