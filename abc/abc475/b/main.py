N = int(input())
A = list(map(int, input().split()))

ans = [0, 0, 0]

for a in A:
    r = a % 1000
    change = (1000 - r) % 1000
    ans[2] += change // 100
    ans[1] += (change // 10) % 10
    ans[0] += change % 10

print(" ".join(map(str, ans)))
