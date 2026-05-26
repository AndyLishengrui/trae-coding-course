n = int(input())
c = r = f = 0
for _ in range(n):
    k, t = input().split()
    k = int(k)
    if t == 'C': c += k
    elif t == 'R': r += k
    else: f += k
s = c + r + f
print(f"Total: {s} animals")
for name, cnt in [('coneys',c),('rats',r),('frogs',f)]:
    print(f"Total {name}: {cnt}")
for name, cnt in [('coneys',c),('rats',r),('frogs',f)]:
    print(f"Percentage of {name}: {cnt/s*100:.2f} %")
