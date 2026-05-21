def factorial(n):
    if n == 1:
        return [1]
    res = [1]
    for i in range(2, n + 1):
        # Multiply each digit by i
        for j in range(len(res)):
            res[j] *= i
        # Handle carry
        t = 0
        for j in range(len(res) - 1, -1, -1):
            temp = t + res[j]
            t = temp // 10
            res[j] = temp % 10
        # Handle remaining carry
        while t:
            res.insert(0, t % 10)
            t //= 10
    return res

def main():
    import sys
    input = sys.stdin.read().split()
    for n_str in input:
        n = int(n_str)
        if n == 1:
            print('1')
        else:
            res = factorial(n)
            print(''.join(map(str, res)))

if __name__ == "__main__":
    main()
