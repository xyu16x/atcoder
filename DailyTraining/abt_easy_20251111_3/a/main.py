s = input()

index1 = s.find("|")
index2 = s[index1 + 1 :].find("|") + index1 + 1

print(s[0:index1] + s[index2 + 1 : len(s)])
