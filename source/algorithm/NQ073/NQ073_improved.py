import sys
def calc():
    tokens = []
    for line in sys.stdin:
        tokens.extend(line.strip().split())
    index = 0
    def helper():
        nonlocal index
        if index >= len(tokens):
            return 0.0
        token = tokens[index]
        index += 1
        if token == '+':
            return helper() + helper()
        elif token == '-':
            return helper() - helper()
        elif token == '*':
            return helper() * helper()
        elif token == '/':
            return helper() / helper()
        else:
            return float(token)
    return helper()
def main():
    res = calc()  # 递归计算波兰表达式
    print(res)

if __name__ == "__main__":
    main()
