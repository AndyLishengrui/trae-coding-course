# NQ006X 数组替换
X = [int(input()) for _ in range(10)]
for i in range(10):
    if X[i] <= 0:
        X[i] = 1
for i in range(10):
    print(f"X[{i}] = {X[i]}")