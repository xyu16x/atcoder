import sys


# 標準入力を高速化
def main():
    contests = ["ABC", "ARC", "AGC", "AHC"]

    s = list(input() for _ in range(3))

    for i in range(3):
        for j in range(len(contests)):
            if s[i] == contests[j]:
                contests.remove(s[i])
                break

    print(contests[0])


if __name__ == "__main__":
    main()
