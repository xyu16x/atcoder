s_list = input()

chars = []

for s in s_list:
    if s not in chars:
        chars.append(s)
    

cnt_chars = [0] * 3
for char in chars:

