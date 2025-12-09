s = input()
t = input()

if s == t:
    print("Yes")
    exit()

for i in range(len(s) - len(t) + 1):
    for j in range(len(t)):
        if t[j] != s[i + j]:
            break
        if j == len(t) - 1:
            print("Yes")
            exit()

print("No")
