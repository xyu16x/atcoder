H, W, Q = map(int, input().split())

# 整数R、下R行のチョコレートのブロックの個数を求め食べる
# 整数C、→C列のチョコレートのブロックの個数を求め食べる

for i in range(Q):
    q = list(input().split())

    if q[0] == "1":  # R
        print(W * int(q[1]))
        H -= int(q[1])
    elif q[0] == "2":  # C
        print(H * int(q[1]))
        W -= int(q[1])
