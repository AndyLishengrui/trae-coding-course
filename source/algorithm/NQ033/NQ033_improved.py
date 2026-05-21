# NQ033 电话号码缩短
# 将电话号码缩短为固定前缀6加上最后5位
def main():
    n = int(input())  # 读取测试用例数量
    for _ in range(n):  # 遍历每个测试用例
        phone = input().strip()  # 读取电话号码
        # 固定前缀6加上原电话号码的最后5位
        short_num = "6" + phone[-5:]
        print(short_num)  # 输出缩短后的电话号码

if __name__ == "__main__":
    main()