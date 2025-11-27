n, x = map(int, input().split())


syou = x // n
amari = x % n


start_code = ord("A")

if amari == 0:
    print(chr(start_code + syou - 1))
else:
    print(chr(start_code + syou))
