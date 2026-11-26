N = int(input())
X = list(map(int, input().split()))

X = sorted(X, reverse=True)
# print(X)

if X[0] >= 0:
    print("No")
else:
    print("Yes")
