# NQ008X 数组选择
A = []
for i in range(100):
    A.append(float(input()))
for i in range(100):
    if A[i] <= 10.0:
        print(f"A[{i}] = {A[i]:.1f}")