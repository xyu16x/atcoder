s = list(map(int, input().split()))

current_max = s[0]

for i in range(len(s)):
    if s[i] >= 100 and s[i] <= 675:
        if s[i] % 25 == 0:
            if i >= 1:
                if s[i] == max(current_max, s[i]):
                    current_max = s[i]
                else:
                    print("No")
                    exit()
        else:
            print("No")
            exit()
    else:
        print("No")
        exit()

print("Yes")
