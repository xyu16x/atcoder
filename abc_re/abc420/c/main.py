n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
query = [list(input().split()) for _ in range(q)]


min = []
w = []
ans = 0

for i in range(n):
    min.append(a[i] if a[i] < b[i] else b[i])
    w.append("a" if a[i] < b[i] else "b")
    ans += a[i] if a[i] < b[i] else b[i]

for qu in query:
    ci = int(qu[1]) - 1
    vi = int(qu[2])
    current = 0

    if qu[0] == "A":
        a[ci] = vi  # a置き換え
        current = min[ci]  # いったん退避
        min[ci] = a[ci] if a[ci] < b[ci] else b[ci]
        ans += min[ci] - current
    elif qu[0] == "B":
        b[ci] = vi  # a置き換え
        current = min[ci]  # いったん退避
        min[ci] = b[ci] if b[ci] < a[ci] else a[ci]
        ans += min[ci] - current
    print(ans)
