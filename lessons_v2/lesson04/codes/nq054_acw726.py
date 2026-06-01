import math
n = int(input())
for i in range(2, n + 1):
    prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)
