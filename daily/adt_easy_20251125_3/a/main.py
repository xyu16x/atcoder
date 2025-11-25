n = int(input())
p = list(map(int, input().split()))

if max(p) != p[0]:
    print(max(p) - p[0] + 1)
elif sum(1 for i in p if i == max(p)) > 1:
    print(1)
else:
    print(0)
