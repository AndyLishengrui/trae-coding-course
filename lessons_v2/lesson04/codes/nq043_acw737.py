# NQ: AcWing 737
arr = [0] * 10
for i in range(10):
    arr[i] = max(1, int(input()))
    print(f"X[{i}] = {arr[i]}")
