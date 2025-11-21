n = int(input())
s = input()
cnt_t = 0
cnt_a = 0

for i in s:
    if i == "T":
        cnt_t += 1
        if cnt_t >= n / 2:
            print("T")
            exit()
    if i == "A":
        cnt_a += 1
        if cnt_a >= n / 2:
            print("A")
            exit()
