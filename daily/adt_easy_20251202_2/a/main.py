n, m = map(int, input().split())
a = list(map(int, input().split()))

total = 0
for i in a:
    total += i
    if total <= m:
        continue
    else:
        print("No")
        exit()

print("Yes")
