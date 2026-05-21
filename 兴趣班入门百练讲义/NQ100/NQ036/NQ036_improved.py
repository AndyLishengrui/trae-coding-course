# NQ036 合并字符串初阶
def main():
    import sys
    input_lines = [line.rstrip('\n') for line in sys.stdin]
    ptr = 0
    t = int(input_lines[ptr])  # 读入测试用例数量
    ptr += 1
    
    for _ in range(t):
        a = input_lines[ptr]  # 读入第一行
        ptr += 1
        b = input_lines[ptr]  # 读入第二行
        ptr += 1
        
        p = len(a) // 2  # 取中点
        # 合并字符串：a的前p个字符 + b + a的后部分
        print(a[:p] + b + a[p:])

if __name__ == "__main__":
    main()