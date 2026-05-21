import sys

for line in sys.stdin:
    # 将所有'5'替换为空格，然后分割成tokens
    tokens = line.strip().replace('5', ' ').split()
    
    nums = []
    for token in tokens:
        # 处理前导零
        if not token:  # 空字符串
            continue
        # 找到第一个非零字符
        start = 0
        while start < len(token) and token[start] == '0':
            start += 1
        if start == len(token):
            nums.append(0)  # 全为0
        else:
            nums.append(int(token[start:]))  # 去除前导零
    
    # 排序并输出
    nums.sort()
    print(' '.join(map(str, nums)))
