list_s = list(map(int, input().split()))

max = 0

for s in list_s:
    if 100 > s or 675 < s:
        print("No")
        exit()
    if s % 25 != 0:
        print("No")
        exit()
    if max > s:
        print("No")
        exit()
    max = s

print("Yes")
