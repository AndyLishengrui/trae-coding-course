def get_divisors(n):
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
        i += 1
    res.sort()
    return res

def main():
    import sys
    n = int(sys.stdin.readline())
    for _ in range(n):
        a = int(sys.stdin.readline())
        res = get_divisors(a)
        print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()
