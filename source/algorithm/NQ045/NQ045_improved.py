import sys

def main():
    for line in sys.stdin:
        s = line.strip()
        if s == "#":
            break
        
        cnt = 0
        length = len(s)
        # 统计前length-1位中'1'的个数
        for i in range(length - 1):
            if s[i] == '1':
                cnt += 1
        
        parity = cnt % 2  # 计算奇偶性
        # 根据校验类型设置校验位
        correct_bit = '1' if ((s[-1] == 'e' and parity == 1) or (s[-1] == 'o' and parity == 0)) else '0'
        print(s[:-1] + correct_bit)

if __name__ == "__main__":
    main()