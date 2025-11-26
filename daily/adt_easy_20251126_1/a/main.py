s = list(map(int, input()))

for i in range(1, len(s), 2):
    if s[i] != 0:
        print("No")
        exit()

print("Yes")
