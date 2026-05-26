# NQ: AcWing 668
a, b, c, d = map(int, input().split())
start = a * 60 + b
end = c * 60 + d
if end <= start:
    end += 24 * 60
diff = end - start
print(f"O JOGO DUROU {diff // 60} HORA(S) E {diff % 60} MINUTO(S)")
