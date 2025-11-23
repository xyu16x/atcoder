n = list(map(int, input().split()))

n.sort(reverse=True)

print("".join(map(str, n)))
