n = int(input())
l = list(map(int, input().split()))

human1 = 0
human2 = n

for i in range(n):
    if l[i] == 1:
        break
    else:
        human1 += 1

for i in range(n - 1, -1, -1):
    if l[i] == 1:
        break
    else:
        human2 -= 1

if human1 >= human2:
    ans = 0
else:
    ans = human2 - human1 - 1

print(ans)
