import heapq

Q = int(input())
hq = []

for _ in range(Q):
    t, h = map(int, input().split())
    if t == 1:
        heapq.heappush(hq, h)
    else:
        while hq and hq[0] <= h:
            heapq.heappop(hq)
    print(len(hq))
