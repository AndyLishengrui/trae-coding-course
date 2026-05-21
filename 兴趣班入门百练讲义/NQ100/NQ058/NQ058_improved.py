# Python代码不需要包含额外的库，因为列表和输入输出都是内置的

# 读取目标和数组长度
target, n = map(int, input().split())

# 读取数组元素并存储到列表中
a = list(map(int, input().split()))

# 双指针算法
i, j = 0, n - 1
while i < j:
    sum_val = a[i] + a[j]
    if sum_val == target:
        print(i, j)
        break
    elif sum_val < target:
        i += 1  # 和小于target，移动左指针
    else:
        j -= 1  # 和大于target，移动右指针

# Python中不需要显式的return 0，程序正常结束即可