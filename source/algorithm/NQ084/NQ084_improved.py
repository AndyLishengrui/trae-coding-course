def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    s_to_t = {}
    t_to_s = {}
    for c1, c2 in zip(s, t):
        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False  # 检查映射是否一致
        else:
            if c2 in t_to_s:
                return False  # 检查是否有重复映射
            s_to_t[c1] = c2
            t_to_s[c2] = c1
    return True

def main():
    import sys
    n = int(sys.stdin.readline())
    for _ in range(n):
        line = sys.stdin.readline().strip()
        s, t = line.split()
        print("true" if is_isomorphic(s, t) else "false")

if __name__ == "__main__":
    main()