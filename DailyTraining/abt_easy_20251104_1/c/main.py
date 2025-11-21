n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = []

for i in a:
    if i in ans:
        continue
    else:
        ans.append(i)

ans = [str(num) for num in ans]

print(len(ans))
print(" ".join(ans))
