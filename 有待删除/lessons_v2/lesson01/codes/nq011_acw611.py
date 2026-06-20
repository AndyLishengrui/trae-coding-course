import sys
data = sys.stdin.read().split()
c, q, p = int(data[0]), int(data[1]), float(data[2])
print(f"VALOR A PAGAR: R$ {q * p:.2f}")
