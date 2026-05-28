import sys
data = sys.stdin.read().split()
for x in data:
    if x == '-1': break
for i in range(len(data)-2, -1, -1):
    if data[i] == '-1': break
    print(data[i])
