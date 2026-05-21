def is_palindrome(x):
    if x < 0:
        return False
    res, oldx = 0, x
    while x:
        res = res * 10 + x % 10
        x //= 10
    return res == oldx

def main():
    import sys
    for line in sys.stdin:
        n = int(line.strip())
        print("true" if is_palindrome(n) else "false")

if __name__ == "__main__":
    main()