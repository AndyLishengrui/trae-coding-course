# NQ: AcWing 718
from collections import Counter
n = int(input())
cnt = Counter()
for _ in range(n):
    k, t = input().split()
    cnt[t] += int(k)
print(f"Total: {sum(cnt.values())} animals")
print(f"Total coneys: {cnt.get('C', 0)}")
print(f"Total rats: {cnt.get('R', 0)}")
print(f"Total frogs: {cnt.get('F', 0)}")
total = sum(cnt.values())
for t, name in [('C', 'coneys'), ('R', 'rats'), ('F', 'frogs')]:
    print(f"Percentage of {name}: {cnt.get(t, 0) / total * 100:.2f} %")
