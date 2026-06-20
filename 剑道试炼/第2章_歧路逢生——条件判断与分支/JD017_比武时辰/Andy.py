a, b = map(int, input().split())
if a < b:
    horas = b - a
else:
    horas = 24 - a + b
print(f"O JOGO DUROU {horas} HORA(S)")