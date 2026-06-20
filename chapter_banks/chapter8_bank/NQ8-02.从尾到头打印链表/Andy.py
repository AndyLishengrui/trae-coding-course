import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    nums = list(map(int, line.split()))
    nums.pop()  # remove -1
    for x in reversed(nums):
        print(x)
