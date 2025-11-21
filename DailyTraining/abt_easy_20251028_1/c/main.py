def main():
    n, m = map(int, input().split())
    s = input()
    t = input()

    flg_h = False
    flg_t = False

    if s == t[: len(s)]:
        flg_h = True
    if s == t[-len(s) :]:
        flg_t = True

    if flg_h and flg_t:
        print(0)
    elif flg_h:
        print(1)
    elif flg_t:
        print(2)
    else:
        print(3)


if __name__ == "__main__":
    main()
