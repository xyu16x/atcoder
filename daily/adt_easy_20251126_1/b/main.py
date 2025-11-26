def main():
    t = int(input())

    ft = func(t)

    ans = func(func((ft + t)) + func(ft))

    print(ans)


def func(x):
    return x * x + 2 * x + 3


if __name__ == "__main__":
    main()
