from collections import defaultdict
import math
import sys

# 再帰の深さの限界を上げる (計算時にエラーを防ぐため)
sys.setrecursionlimit(3000)


def solve():
    # 入力処理
    try:
        # N, M を読み込む
        N, M = map(int, sys.stdin.readline().split())

        # 数列 A を読み込む
        A = list(map(int, sys.stdin.readline().split()))
    except:
        # 入力がない場合の安全策
        return

    # 全ての L (1から10桁まで) について処理を行う
    # 10^9 は最大10桁なので、Lは1から10まで
    MAX_DIGITS = 10
    total_count = 0

    # 1. 桁数ごとの処理
    for L in range(1, MAX_DIGITS + 1):

        # P_L: 10^L mod M を計算 (A_i の係数)
        # pow(10, L, M) は (10 ** L) % M を高速に計算する
        P_L = pow(10, L, M)

        # 辞書: count_R[R_j] は R_j の値をとる A_j の個数
        # R_j = (-A_j) mod M
        count_R = defaultdict(int)

        # 2. A_j の処理: 右辺 R_j = (-A_j) mod M のカウント
        for a_j in A:
            # A_j の桁数が L と一致する場合のみ対象
            # 桁数は math.floor(math.log10(a_j)) + 1 で計算
            if L == len(str(a_j)):
                # R_j = (-A_j) mod M を計算
                # Pythonの % 演算子は結果が非負になるように配慮されているため、
                # (M - (a_j % M)) % M で正確な正の剰余を取得する
                R_j = (M - (a_j % M)) % M
                count_R[R_j] += 1

        # 3. A_i の処理: 左辺 L_i = (A_i * P_L) mod M と R_j が一致する組を探索
        for a_i in A:
            # L_i = (A_i * 10^L) mod M を計算
            # P_L = 10^L mod M は既に計算済み
            L_i = (a_i * P_L) % M

            # 条件: L_i == R_j
            # L_i と等しい R_j の値を持つ A_j の個数を total_count に加算する
            if L_i in count_R:
                total_count += count_R[L_i]

    # 結果の出力
    print(total_count)


if __name__ == "__main__":
    solve()
