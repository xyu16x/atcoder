K = int(input())
A = list(map(int, input().split()))

nine_flg = A.count(9)
ball_min = min(A)

if nine_flg != 0:
    print(ball_min)
else:
    print(-1)
