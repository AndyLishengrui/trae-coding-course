# NQ028 0-1矩阵统计
# 统计矩阵中值为1的元素个数
def main():
    t = int(input())  # 读取测试用例数量
    for _ in range(t):  # 遍历每个测试用例
        a, b = map(int, input().split())  # 读取矩阵的行数a和列数b
        cnt = 0  # 初始化计数器
        for i in range(a):  # 遍历矩阵的每一行
            row = list(map(int, input().split()))  # 读取一行元素
            cnt += row.count(1)  # 统计当前行中1的个数并累加
        print(cnt)  # 输出统计结果

if __name__ == "__main__":
    main()