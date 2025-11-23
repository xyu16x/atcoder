k = int(input())

ans = []
start_code = ord("A")

for i in range(k):
    ans.append(chr(start_code + i))

print("".join(ans))
