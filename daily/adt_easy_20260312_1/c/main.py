N, D = map(int, input().split())
S = list(input().strip())

box = N - 1
d = 0

while d < D:
    for i in range(box, -1, -1):
        if S[i] == "@":
            S[i] = "."
            d += 1
            box = i
            break

print("".join(S))
