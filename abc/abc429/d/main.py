n = map(int, input().split())

w = []
h = []
b = []

for _ in range(n):
    w_, h_, b_ = map(int, input().split())
    w.append(w_)
    h.append(h_)
    b.append(b_)

h.sort()
b.sort()

i = n - 1
j = n - 1
ans = 0

while i >= 0 and j >= 0:
    if h[i] <= b[i]:
        ans += 0

print(ans)
