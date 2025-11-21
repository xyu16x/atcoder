def main():
    n = int(input())

    if n >= 42:
        n += 1

    if n < 10:
        res = "00" + str(n)
    elif n < 100:
        res = "0" + str(n)
    else:
        res = str(n)

    print("AGC" + res)


if __name__ == "__main__":
    main()
