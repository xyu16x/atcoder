def main():
    n, x, y, z = map(int, input().split())

    if x > y:
        if x > z and y <= z:
            print("Yes")
        else:
            print("No")
    else:
        if x < z and y >= z:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
