l = int(input())
t = input().strip()
sum_val = 0
for i in range(12):
    for j in range(12):
        x = float(input())
        if i == l: sum_val += x
print(f"{sum_val if t == 'S' else sum_val / 12:.1f}")
