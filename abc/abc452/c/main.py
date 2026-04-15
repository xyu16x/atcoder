# オブジェ: N本の肋骨、1本の脊髄
# 肋骨:1 - N
# 文字:脊髄N文字、肋骨i Ai文字、Bi文字目=脊髄のi文字目

N = int(input())
A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

M = int(input())
S = [input().strip() for _ in range(M)]

chars = [set() for _ in range(N)]

for s in S:
    l = len(s)
    for i in range(N):
        if l == A[i]:
            chars[i].add(s[B[i] - 1])

for s in S:
    if len(s) != N:
        print("No")
        continue
    flg = True
    for i in range(N):
        if s[i] not in chars[i]:
            flg = False
            break
    print("Yes" if flg else "No")
