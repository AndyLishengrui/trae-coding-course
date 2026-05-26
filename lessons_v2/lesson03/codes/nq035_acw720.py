# NQ: AcWing 720
a, n = map(int, input().split())
while n <= 0:
    n = int(input())
print(sum(a + i for i in range(n)))
