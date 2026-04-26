N, M = map(int, input().split())
F = list(map(int, input().split()))

clothes = set()

for f in F:
    clothes.add(f)

if len(clothes) == N:
    print("Yes")
else:
    print("No")

if len(clothes) == M:
    print("Yes")
else:
    print("No")
