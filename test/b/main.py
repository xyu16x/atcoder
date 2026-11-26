import sys


# 標準入力を高速化
def main(text):
    S = list(text.split())

    ans = 0

    for s in S:
        if s[0].isupper():
            ans += 1

    # return ans
    print(ans)


if __name__ == "__main__":
    main(input())
