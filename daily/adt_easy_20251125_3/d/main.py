n = int(input())
s = list(map(int, input().split()))

ans = [i for i in range(n)]

for a in range(1, 15):
    for b in range(a, 142):
        delete = []
        for an in ans:
            if 3 * (a + b) + (4 * a * b) == s[an]:
                delete.append(an)
        ans = [i for i in ans if i not in delete]

print(len(ans))
