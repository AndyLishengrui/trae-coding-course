import sys

def is_humble_number(x):
    res = x
    while res % 2 == 0:
        res //= 2
    while res % 3 == 0:
        res //= 3
    while res % 5 == 0:
        res //= 5
    while res % 7 == 0:
        res //= 7
    return res == 1

def main():
    N = 6007
    a = [0] * N
    k = 1
    for i in range(1, 20000000):
        if is_humble_number(i):
            a[k] = i
            k += 1
            if k >= N:
                break
    q = int(sys.stdin.readline())
    for _ in range(q):
        idx = int(sys.stdin.readline())
        print(a[idx])

if __name__ == "__main__":
    main()
