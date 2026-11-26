N, X = input().split()
N = int(N)
S = [list(input().strip()) for _ in range(N)]

X = ord(X) - ord("A")

for n in range(N):
    if S[n][X] == "o":
        print("Yes")
        exit()

print("No")
