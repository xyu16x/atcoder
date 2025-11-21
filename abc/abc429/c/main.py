n, m, k = map(int, input().split())
h = list(map(int, input().split()))
b = list(map(int, input().split()))

h.sort()
b.sort()

i = 0
j = 0
cnt = 0

while i < n and j < m:
    if h[i] <= b[j]:
        cnt += 1
        i += 1
        j += 1
        if cnt == k:
            print("Yes")
            exit()
    else:
        j += 1

if cnt >= k:
    print("Yes")
else:
    print("No")
