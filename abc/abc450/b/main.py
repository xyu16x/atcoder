n = int(input())
C = []


for i in range(n - 1):
    c = list(map(int, input().split()))
    C.append(c)

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if C[i][j - i - 1] + C[j][k - j - 1] < C[i][k - i - 1]:
                print("Yes")
                exit()

print("No")
