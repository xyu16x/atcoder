S = input()

cnt_e = 0
cnt_w = 0

for s in S:
    if s == "E":
        cnt_e += 1
    else:
        cnt_w += 1

if cnt_e > cnt_w:
    print("East")
else:
    print("West")
