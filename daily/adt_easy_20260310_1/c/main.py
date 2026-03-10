s1, s2 = input().strip()
t1, t2 = input().strip()

list = ["A", "B", "C", "D", "E"]
s1, s2, t1, t2 = list.index(s1), list.index(s2), list.index(t1), list.index(t2)

dist_s = abs(s1 - s2) if abs(s1 - s2) <= 2 else 5 - abs(s1 - s2)
dist_t = abs(t1 - t2) if abs(t1 - t2) <= 2 else 5 - abs(t1 - t2)

if dist_s == dist_t:
    print("Yes")
else:
    print("No")
