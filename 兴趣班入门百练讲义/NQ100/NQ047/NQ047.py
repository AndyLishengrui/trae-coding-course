def sum_of_unique(a, size):
    # 创建一个集合用于存储唯一值
    unique_values = set()
    # 遍历数组
    for i in range(size):
        # 将数组中的元素添加到集合中，若元素已存在则不会添加
        unique_values.add(a[i])
    # 返回集合中唯一值的个数
    return len(unique_values)

def main():
    n, size = map(int, input().split()) # 读取数组的长度和需要计算的前缀大小
    a = list(map(int, input().split()))[:n] # 读取数组元素，并截取前n个
    result = sum_of_unique(a, size) # 调用函数计算唯一值的数量
    print(n - size + result) # 输出结果

if __name__ == "__main__":
    main()