def main():
    n, q = map(int, input().split())
    x = list(map(int, input().split()))

    ans = [0] * q
    ball = [0] * n

    for i in range(q):
        if x[i] >= 1:
            ans[i] = x[i]
            ball[x[i] - 1] += 1
        else:
            box = 0
            min = q
            for j in range(n):
                if ball[j] < min:
                    min = ball[j]
                    box = j
            ans[i] = box + 1
            ball[box] += 1

    print(*ans)


if __name__ == "__main__":
    main()
