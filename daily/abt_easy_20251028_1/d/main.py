def main():
    n, m = map(int, input().split())
    x = 10**9

    if m != 0 and n >= x:
        print("inf")
        exit()

    ans = 0

    for i in range(m + 1):
        ans += n**i
        if ans > x:
            print("inf")
            exit()

    print(ans)


if __name__ == "__main__":
    main()
