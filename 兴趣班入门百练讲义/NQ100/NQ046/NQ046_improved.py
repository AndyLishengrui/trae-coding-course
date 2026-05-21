import sys

def main():
    for line in sys.stdin:
        top = float(line.strip())
        if top == 0:
            break
        
        res = 0.0
        cnt = 1
        
        # 计算调和级数的和，直到超过top
        while res < top:
            res += 1.0 / (2.0 * cnt)
            cnt += 1
        
        # 输出结果，注意单复数形式
        blocks = cnt - 1
        print("{0} {1}".format(blocks, "block" if blocks == 1 else "blocks"))

if __name__ == "__main__":
    main()