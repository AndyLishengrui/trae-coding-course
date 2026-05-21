def main():
    import sys
    q = int(sys.stdin.readline().strip())
    while q > 0:
        diffs = []
        line = sys.stdin.readline().strip()
        n, k = map(int, line.split())
        line = sys.stdin.readline().strip()
        a = list(map(int, line.split()))
        for i in range(n-1):
            for j in range(i+1, n):
                diff = abs(a[i] - a[j])
                diffs.append(diff)  # 计算所有可能的差
        diffs.sort(reverse=True)  # 降序排序
        unique_diffs = []
        seen = set()
        for d in diffs:
            if d not in seen:
                seen.add(d)
                unique_diffs.append(d)  # 去重
        if k <= len(unique_diffs):
            print(unique_diffs[k-1])  # 输出第K大的差
        else:
            print("Invalid k value!")
        q -= 1

if __name__ == "__main__":
    main()