from collections import deque

N = int(input())

time = set()
ppl = {}

for _ in range(N):
    H, L = map(int, input().split())
    time.add(L)
    if L not in ppl:
        ppl[L] = H
    else:
        ppl[L] = max(ppl[L], H)

time = deque(sorted(time))

Q = int(input())
T = list(map(int, input().split()))

Ti = [(v, i) for i, v in enumerate(T)]
Ti = sorted(Ti, key=lambda x: x[0])

maxi = []

for _, (v, i) in enumerate(Ti):
    while time and v >= time[0]:
        del ppl[time[0]]
        time.popleft()
    maxi.append((max(ppl.values()), i))

maxi.sort(key=lambda x: x[1])
ans = [v for v, _ in maxi]

for a in ans:
    print(a)
