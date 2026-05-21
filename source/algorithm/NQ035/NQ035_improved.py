# NQ035 二进制字符串奇偶位互换
# 将二进制字符串的相邻两位（奇偶位）互换位置
def main():
    test_case_count = int(input())  # 读取测试用例数量
    
    for _ in range(test_case_count):  # 遍历每个测试用例
        binary_str = input().strip()  # 读取二进制字符串
        chars = list(binary_str)  # 转换为字符列表以便修改
        
        # 每两位互换位置（奇偶位互换）
        # 遍历步长为2，每次处理i和i+1位置的字符
        for i in range(0, len(chars) - 1, 2):
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
        
        print(''.join(chars))  # 转换回字符串并输出

if __name__ == "__main__":
    main()