# 质数标记数组，p[i]为True表示i是质数
p = [False] * 100
# 初始化质数表
p[2] = p[3] = p[5] = p[7] = p[11] = True
p[13] = p[17] = p[19] = p[23] = p[29] = True
p[31] = p[37] = True

now = 0

def dfs(deep, n, a, used):
    if deep == n and p[a[0] + a[-1]]:
        print(' '.join(map(str, a)))
        return
    for i in range(2, n + 1):
        if not used[i] and p[i + a[-1]]:
            used[i] = True
            a.append(i)
            dfs(deep + 1, n, a, used)  # 递归搜索下一个位置
            a.pop()  # 回溯
            used[i] = False  # 回溯

def main():
    global now
    first_case = True
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if not first_case:
            print()
        first_case = False
        now += 1
        print("Case {}:".format(now))
        used = [False] * (n + 1)
        a = [1]  # 第一个元素固定为1
        used[1] = True
        dfs(1, n, a, used)  # 从第二个位置开始DFS

if __name__ == "__main__":
    main()
