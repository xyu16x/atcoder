s = input()
t = input()

diff_index = []

for i in range(len(s)):
    if s[i] != t[i]:
        diff_index.append(i)

if len(diff_index) == 0:
    print("Yes")
elif len(diff_index) == 2:
    i1 = diff_index[0]
    i2 = diff_index[1]
    check_index = abs(i1 - i2) == 1
    check_swap = (s[i1] == t[i2]) and (s[i2] == t[i1])

    if check_index and check_swap:
        print("Yes")
    else:
        print("No")
else:
    print("No")
