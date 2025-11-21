n = int(input())
a = list(map(int, input().split()))

a_sort = sorted(a, reverse=True)

ans_score = a_sort[1]

print(a.index(ans_score) + 1)
