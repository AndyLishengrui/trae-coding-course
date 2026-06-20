n, size = map(int, input().split())
a = list(map(int, input().split()))
a[:size] = reversed(a[:size])
print(' '.join(map(str, a)))
