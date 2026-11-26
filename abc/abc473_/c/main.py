import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

members = [0 for _ in range(K)]

for a in A:
    members[a - 1] += 1

members.sort(reverse=True)
target = members[0] - 1

left = 0
right = K - 1
# print(members)

while left < right:
    mid = (left + right + 1) // 2
    # print(left, right, mid)

    if members[mid] >= target:
        left = mid
    else:
        right = mid - 1

# print(left, right, mid)

print(left + 1)
