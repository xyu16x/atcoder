def main():
    t = int(input())

    for i in range(t):
        n, h = map(int, input().split())
        case = [list(map(int, input().split())) for _ in range(n)]
        res = solve(n, h, case)
        print("Yes") if res else print("No")


def solve(n, h, case):
    t = 0
    f_min = h
    f_max = h

    for i in range(n):
        ti = case[i][0]
        li = case[i][1]
        ui = case[i][2]

        delta_t = ti - t
        f_min -= delta_t
        f_max += delta_t

        if f_min <= 0:
            f_min = 1

        t = ti
        f_min = max(f_min, li)
        f_max = min(f_max, ui)

        if f_min > f_max:
            return False

    return True


if __name__ == "__main__":
    main()
