p, q = input().split()

dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
distance = [3, 1, 4, 1, 5, 9]

p = dict.get(p)
q = dict.get(q)

ans = 0

if p > q:
    for i in range(q, p):
        ans += distance[i]
else:
    for i in range(p, q):
        ans += distance[i]

print(ans)
