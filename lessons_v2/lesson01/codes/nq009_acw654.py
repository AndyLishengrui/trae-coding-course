# NQ: AcWing 654
n = int(input())
h, r = divmod(n, 3600)
m, s = divmod(r, 60)
print(f"{h}:{m}:{s}")
