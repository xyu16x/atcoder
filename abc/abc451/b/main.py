N, M = map(int, input().split())

a_list = [0 for _ in range(M)]
b_list = [0 for _ in range(M)]

for i in range(N):
    A, B = map(int, input().split())

    a_list[A - 1] += 1
    b_list[B - 1] += 1

for i in range(M):
    print(b_list[i] - a_list[i])
