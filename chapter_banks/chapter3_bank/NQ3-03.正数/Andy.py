import sys
nums = list(map(float, sys.stdin.read().split()))
cnt = sum(1 for x in nums if x > 0)
print(f"{cnt} positive numbers")
