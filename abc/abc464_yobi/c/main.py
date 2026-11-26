N, M = map(int, input().split())

Birds = []
count = [0] * (N + 1)

for _ in range(N):
    A, D, B = map(int, input().split())
    Birds.append([A, D, B])
    count[A] += 1

Birds.sort(key=lambda x: x[1])
kinds = sum(1 for c in count if c > 0)

index = 0

for d in range(1, M + 1):
    while index < N and Birds[index][1] == d:
        A, D, B = Birds[index]
        count[A] -= 1
        if count[A] == 0:
            kinds -= 1
        count[B] += 1
        if count[B] == 1:
            kinds += 1
        index += 1
    print(kinds)
