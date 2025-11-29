n = int(input())
cloud = [list(map(int, input().split())) for _ in range(n)]

sky = [[0] * 2000] * 2000

ans = 2000 * 2000
