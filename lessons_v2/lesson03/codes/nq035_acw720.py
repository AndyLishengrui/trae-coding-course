a = int(input())
while True:
    for n in map(int, input().split()):
        if n > 0: break
    if n > 0: break
print(sum(a + i for i in range(n)))
