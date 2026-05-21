def is_ugly(num):
    if num <= 0:
        return False
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5
    return num == 1

def main():
    import sys
    for line in sys.stdin:
        n = int(line.strip())
        print("true" if is_ugly(n) else "false")

if __name__ == "__main__":
    main()