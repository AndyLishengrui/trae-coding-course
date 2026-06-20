while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0: break
    if m > n: m, n = n, m
    nums = range(m, n + 1)
    print(' '.join(map(str, nums)), f"Sum={sum(nums)}")
