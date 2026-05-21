# NQ038 统计数字字符个数
def main():
    import sys
    input_lines = [line.rstrip('\n') for line in sys.stdin]
    ptr = 0
    test_case_num = int(input_lines[ptr])
    ptr += 1
    
    for _ in range(test_case_num):
        if ptr >= len(input_lines):
            break
        input_line = input_lines[ptr]
        ptr += 1
        
        digit_count = sum(1 for c in input_line if c.isdigit())  # 统计数字字符个数
        print(digit_count)

if __name__ == "__main__":
    main()