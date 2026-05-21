# Python 3.5 不支持变量的类型提示，所以在这里我们省略它们

def main():
    q = int(input().strip())  # 读取测试用例的数量
    while q:
        n, k = map(int, input().strip().split())  # 读取当前测试用例的 n 和 k
        a = list(map(int, input().strip().split()))  # 读取整数数组
        nums = []  # 初始化一个空列表来存储绝对差值

        # 计算绝对差值并添加到 nums 中
        for i in range(n - 1):
            for j in range(i + 1, n):
                nums.append(abs(a[i] - a[j]))

        # 降序排序并去除重复项
        nums = sorted(set(nums), reverse=True)

        # 检查 k 是否在结果列表的范围内
        if k <= len(nums):
            print(nums[k - 1])  # 输出第 k 大的元素
        else:
            print("无效的 k 值")  # 如果 k 超出范围，则输出错误消息

        q -= 1  # 减少剩余测试用例的数量

if __name__ == "__main__":
    main()