n, q = map(int, input().split())  # n:ボール
a = list(map(int, input().split()))  # ボールiに書かれている整数Ai

# query[1]: 取り出すk個
# query[2]: 取り出すボールB1, B2, ... , Bn
# 出力 袋に残ったボールの整数の最小値を出力
# 戻す

cnt = 0
min_list = []

a_sorted = sorted(a)
first_six = a_sorted[:6]


for i in range(q):
    k = int(input())
    b = list(map(int, input().split()))
    new_first_six = first_six[:]

    for i in range(k):
        if a[b[i] - 1] in first_six:
            new_first_six.remove(a[b[i] - 1])

    print(min(new_first_six))
