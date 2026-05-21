# NQ031 解密问题
# 对输入的文本进行解密，将大写字母左移5位
def main():
    import sys
    is_awaiting = False  # 标记是否正在等待解密文本
    
    for line in sys.stdin:
        line = line.rstrip('\n')
        if line == "ENDOFINPUT":
            break  # 遇到结束标志，退出循环
        if line == "START":
            is_awaiting = True  # 遇到开始标志，准备接收解密文本
            continue
        if is_awaiting:
            decrypted = []  # 存储解密后的字符
            for c in line:
                if 'A' <= c <= 'Z':
                    # 左移5位等价于右移21位（26-5=21）
                    decrypted_char = chr(ord('A') + (ord(c) - ord('A') + 21) % 26)
                    decrypted.append(decrypted_char)
                else:
                    decrypted.append(c)  # 非大写字母保持不变
            print(''.join(decrypted))  # 输出解密后的文本
            is_awaiting = False  # 重置标志

if __name__ == "__main__":
    main()