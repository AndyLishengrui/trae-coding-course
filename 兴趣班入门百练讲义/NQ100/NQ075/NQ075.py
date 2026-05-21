# Python 3.5 does not have a specific version constraint on this code

# Constants
MAX_DIGITS = 1007  # P进制位最多位数 (not used in Python version)
P = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # P进制字符映射表

# 将十进制数n转换为p进制，并返回转换后的字符串
def DecimalToP(n, p):
    if n == 0:
        return "0"  # 处理n为0的特殊情况

    result = ""
    is_negative = False

    if n < 0:
        is_negative = True
        n = -n

    while n > 0:
        result = P[n % p] + result  # 不断取余并构建结果字符串
        n //= p

    if is_negative:
        result = "-" + result  # 如果是负数，添加负号
    return result

# 主程序
def main():
    try:
        while True:
            # 输入n和p，使用input替代cin，并用split()分割字符串
            input_str = input().split()
            n = int(input_str[0])
            p = int(input_str[1])
            if p < 2 or p > 36:
                print("Error: Invalid base input.")  # 输出错误信息
                continue

            print(DecimalToP(n, p))  # 输出转换后的p进制数
    except EOFError:
        pass  # 处理EOF情况，在Python中通常用于文件结束或Ctrl+D输入

if __name__ == "__main__":
    main()