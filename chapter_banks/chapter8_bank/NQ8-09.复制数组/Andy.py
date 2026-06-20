n, m, size = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b[:size] = a[:size]
print(' '.join(map(str, b)))
