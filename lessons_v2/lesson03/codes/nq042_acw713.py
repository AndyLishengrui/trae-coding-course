n = int(input())
in_cnt = sum(1 for _ in range(n) if 10 <= int(input()) <= 20)
print(f"{in_cnt} in")
print(f"{n - in_cnt} out")
