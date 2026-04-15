n = int(input())
qr = [list(map(int, input().split())) for _ in range(n)]
Q = int(input())
# td = [list(map(int, input().split())) for _ in range(q)]

# N種類のごみ
# i種類目のごみ　日付Qiで割ったあまりがriの日に収集
# Q個の質問に答える

for i in range(Q):
    t, d = map(int, input().split())
    q, r = qr[t - 1][0], qr[t - 1][1]

    dd = d % q
    dw = d // q

    if dd <= r:
        print(q * dw + r)
    else:
        print(q * (dw + 1) + r)
