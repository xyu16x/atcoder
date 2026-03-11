s = list(map(int, input().split()))


cnt_a = s.count(s[0])

if cnt_a >= 4:
    print("No")
    exit()
else:
    b = 0
    cnt_b = 0
    for i in s:
        if i != s[0]:
            cnt_b += 1
            if cnt_b == 1:
                b = i
            if b != i:
                print("No")
                exit()

print("Yes")
