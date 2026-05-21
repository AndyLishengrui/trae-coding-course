def sum_of_unique(a, size):
    unique_values = set()  # 存储唯一值的集合
    for i in range(size):
        unique_values.add(a[i])  # 添加元素，自动去重
    return len(unique_values)  # 返回唯一值数量

def main():
    n, size = map(int, input().split())  # 读取数组长度和前缀大小
    a = list(map(int, input().split()))[:n]  # 读取数组元素并截取前n个
    unique_count = sum_of_unique(a, size)  # 计算前缀中唯一值数量
    print(n - size + unique_count)  # 输出结果

if __name__ == "__main__":
    main()