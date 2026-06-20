n = int(input())
# All perfect numbers up to 10^8: 6, 28, 496, 8128, 33550336
perfect = [6, 28, 496, 8128, 33550336]
for p in perfect:
    if p <= n:
        print(p)
