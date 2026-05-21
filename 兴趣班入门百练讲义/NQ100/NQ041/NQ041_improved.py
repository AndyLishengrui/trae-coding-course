# NQ041 统计字符个数初步
def main():
    import sys
    input_lines = [line.rstrip('\n') for line in sys.stdin]
    ptr = 0
    n = int(input_lines[ptr])
    ptr += 1
    vowels = ['a', 'e', 'i', 'o', 'u']  # 元音字母列表
    for t in range(n):
        if ptr >= len(input_lines):
            break
        str_input = input_lines[ptr]
        ptr += 1
        str_lower = str_input.lower()  # 将字符串全部转换为小写
        counts = {vowel: 0 for vowel in vowels}
        for c in str_lower:
            if c in counts:
                counts[c] += 1
        for vowel in vowels:
            print("{0}:{1}".format(vowel, counts[vowel]))
        if t < n - 1:
            print()  # 测试用例之间用空行分隔

if __name__ == "__main__":
    main()