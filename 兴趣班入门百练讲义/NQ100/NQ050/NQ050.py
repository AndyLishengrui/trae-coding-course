import sys

# 为了提高输入效率，尤其是在处理大量分散在多行的整数时，
# 我们使用一个生成器来迭代标准输入流中的所有整数。

def get_ints_from_input():
    """
    生成器：从标准输入流中逐个产生整数。
    这种方式高效地模拟了 C++ 中 cin >> num 的行为，自动处理空格和换行。
    """
    # 使用 sys.stdin 迭代器逐行读取，防止一次性读取全部输入导致内存或性能问题
    for line in sys.stdin:
        if not line: 
            break
        # 拆分行并尝试转换为整数
        for item in line.split():
            try:
                yield int(item)
            except ValueError:
                # 忽略无法转换为整数的部分
                continue

def solve():
    """
    主函数：处理 T 组测试用例，每组数据进行排序并输出。
    """
    # 实例化整数生成器
    num_iterator = get_ints_from_input()
    
    try:
        # 读取测试用例的数量 T
        T = next(num_iterator)
    except StopIteration:
        # 输入为空或无法读取 T
        return
    except Exception:
        # 处理输入格式错误
        return
    
    output_lines = []
    
    # 循环处理 T 组数据
    for _ in range(T):
        try:
            # 1. 读取当前数组的元素个数 N
            N = next(num_iterator)
        except StopIteration:
            # 输入提前结束
            break
        
        if N == 0:
            output_lines.append("")
            continue
            
        # 2. 读取 N 个整数
        nums = []
        try:
            # 使用列表推导或 next() 快速收集 N 个数字
            for _ in range(N):
                nums.append(next(num_iterator))
        except StopIteration:
            # 如果数字不足 N 个，通常表示输入不完整，退出处理
            break
            
        # 3. 核心逻辑：使用 Python 内置的 list.sort() 进行原地排序
        # Timsort 算法，时间复杂度为 O(N log N)，高效稳定。
        nums.sort()
        
        # 4. 格式化输出
        # 使用 ' '.join(map(str, nums)) 快速生成空格分隔的字符串
        output_lines.append(' '.join(map(str, nums)))
        
    # 集中输出所有结果，减少 I/O 调用次数，提高整体效率
    sys.stdout.write('\n'.join(output_lines) + '\n')

if __name__ == "__main__":
    solve()