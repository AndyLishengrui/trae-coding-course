# NQ039 合法标识符
def main():
    import sys
    input_data = [line.strip() for line in sys.stdin]
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    for _ in range(n):
        if ptr >= len(input_data):
            break
        s = input_data[ptr]
        ptr += 1
        if s[0].isdigit():
            print("no")
            continue
        valid = True
        for c in s:
            if not (c.isdigit() or c.isalpha() or c == '_'):
                valid = False
                break
        print("yes" if valid else "no")

if __name__ == "__main__":
    main()