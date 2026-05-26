# NQ: AcWing 667
a, b = map(int, input().split())
if a < b:
    print(f"O JOGO DUROU {b - a} HORA(S)")
else:
    print(f"O JOGO DUROU {b - a + 24} HORA(S)")
