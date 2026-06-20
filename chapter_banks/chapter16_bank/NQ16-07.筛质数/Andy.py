import sys
n = int(sys.stdin.read().split()[0])
st = [False] * (n + 1)
primes = []
for i in range(2, n + 1):
    if not st[i]:
        primes.append(i)
    for p in primes:
        if p * i > n: break
        st[p * i] = True
        if i % p == 0: break
print(len(primes))
