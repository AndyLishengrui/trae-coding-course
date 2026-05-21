def main():
    import sys
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        
        max_char = max(s)  # 找到最大字符
        result = []
        for c in s:
            result.append(c)
            if c == max_char:
                result.append("(max)")
        
        print(''.join(result))

if __name__ == "__main__":
    main()