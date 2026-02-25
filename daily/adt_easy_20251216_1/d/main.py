x = int(input())

ans = 1
ans_kaijo = 1

while ans_kaijo <= x:
    ans += 1
    ans_kaijo *= ans
    if ans_kaijo == x:
        print(ans)
        exit()
