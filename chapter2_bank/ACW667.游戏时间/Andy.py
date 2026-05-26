a, b = map(int, input().split())
if a < b:
    d = b - a
else:
    d = b - a + 24
print(f"O JOGO DUROU {d} HORA(S)")
