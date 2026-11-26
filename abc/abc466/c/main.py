N = int(input())

ans = 0

i = 1
j = 2

reverse_flg = False

while i < j or j != N + 1:
    print("? {i} {j}")
    res = input()

    if res == "Yes" and not reverse_flg:
        ans += j - i
        j += 1
    elif res == 'Yes' and reverse_flg:
        ans += 1
        
    elif res == "No":
        reverse_flg = True
        if j == i+1:
            i+= 1
            j += 1
        i = j-1
    elif 