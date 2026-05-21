def f(x):
    """定义函数 f(x) = x^3 - 5x^2 + 10x - 80"""
    return x ** 3 - 5 * x ** 2 + 10 * x - 80

def binary_search(left, right, eps=1e-9):
    """二分法求根"""
    while right - left > eps:
        mid = left + (right - left) / 2
        if f(mid) > 0:
            right = mid  # 根在左半区间
        else:
            left = mid  # 根在右半区间
    return (left + right) / 2  # 返回区间中点作为最终近似根

def main():
    # 在区间 [0, 10] 内求根
    root = binary_search(0.0, 10.0)
    print("{0:.9f}".format(root))

if __name__ == "__main__":
    main()