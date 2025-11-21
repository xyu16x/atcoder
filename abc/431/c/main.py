n, a, b = map(int, input().split())
s = input()

l = 0
r = 0
ans = []
a_cnt = 0
b_cnt = 0

## 二分探索

for i in range(n):
    print(i, s[i])
    if s[i] == "a":
        a_cnt += 1
    if s[i] == "b":
        b_cnt += 1

    r = i

    if a_cnt >= a:
        if b_cnt < b:
            print("append", i, l, r)
            ans.append([l, r])
            if a_cnt > 4:
                for j in range(l, i):
                    l_dash = l + j + 1
                    if s[j] == "b":
                        b_cnt -= 1
                    if s[j] == "a":
                        a_cnt -= 1
                    if a_cnt >= a and b_cnt < b:
                        print("append", i, l_dash, r)
                        ans.append([l_dash, r])
                    if a_cnt < a:
                        break
        else:
            for j in range(l, i):
                l = j + 1
                if s[j] == "b":
                    b_cnt -= 1
                    break
                if s[j] == "a":
                    a_cnt -= 1

print(len(ans))
