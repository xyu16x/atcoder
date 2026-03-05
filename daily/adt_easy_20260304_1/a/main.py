n = int(input())
s = input()

i = 0

while i < n - len(s):
    s = "o" + s

print(s)
