# NQ: AcWing 740
arr = [int(input()) for _ in range(20)]
for i in range(10):
    arr[i], arr[19-i] = arr[19-i], arr[i]
for i, x in enumerate(arr):
    print(f"N[{i}] = {x}")
