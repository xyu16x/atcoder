def rot90(g):
    H, W = len(g), len(g[0])
    return [[g[H - 1 - j][i] for j in range(H)] for i in range(W)]


def flip(g):
    return [row[::-1] for row in g]


def all_transforms(g):
    r0 = g
    r90 = rot90(r0)
    r180 = rot90(r90)
    r270 = rot90(r180)
    f0 = flip(r0)
    f90 = flip(r90)
    f180 = flip(r180)
    f270 = flip(r270)
    return [r0, r90, r180, r270, f0, f90, f180, f270]


N = int(input())
HANDS = []

for _ in range(N):
    H, W = map(int, input().split())
    HAND = [list(input().strip()) for _ in range(H)]

    same = False

    for prev in HANDS:
        for t in all_transforms(prev):
            if len(t) == len(HAND) and len(t[0]) == len(HAND[0]):
                # print(t, HAND)
                if t == HAND:
                    same = True
                    break
        if same:
            break

    if not same:
        HANDS.append(HAND)
    # else:
    #    print("same")


print(len(HANDS))
