# NQ034 求小数点后的数
def main():
    import sys
    input = sys.stdin.read().split()  # 读取所有输入并分割
    ptr = 0  # 当前处理位置指针
    n = int(input[ptr])  # 读取测试用例数量
    ptr += 1
    
    while n > 0:  # 循环n次
        n -= 1
        a = float(input[ptr])  # 输入的浮点数
        t = int(input[ptr + 1])  # 乘以10的次数
        ptr += 2
        
        # 循环t次，每次将a乘以10
        while t > 0:
            t -= 1
            a *= 10.0
        
        # 将a转化为整数后取模10，并输出
        # 加上1e-9避免浮点数精度问题（如9.999999999999被误判为9）
        print(int(a + 1e-9) % 10)

if __name__ == "__main__":
    main()