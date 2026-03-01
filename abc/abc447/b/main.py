s = input()

count = {}

for char in s:
    count[char] = count.get(char, 0) + 1

max_count = max(count.values())

max_char = [k for k, v in count.items() if v == max_count]

ans = []

if len(max_char) == 0:
    print("")
else:
    for char in s:
        if char not in max_char:
            ans.append(char)
    print("".join(ans))
