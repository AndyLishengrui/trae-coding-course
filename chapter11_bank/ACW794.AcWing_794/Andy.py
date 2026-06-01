import sys
sys.set_int_max_str_digits(1000000)
data = sys.stdin.read().split()
a = int(data[0])
b = int(data[1])
print(a // b)
print(a % b)