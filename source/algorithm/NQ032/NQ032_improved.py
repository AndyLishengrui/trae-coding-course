# NQ032 文本格式化
def main():
    import sys
    for line in sys.stdin:  # 逐行读取输入
        line=line.rstrip('\n')
        line_length=len(line)
        if line_length==0:  # 处理空行
            print()
            continue
        line=line[0].upper()+line[1:]  # 首字母大写
        for i in range(line_length-1):  # 处理剩余字符
            if line[i]==' ' and i+1<line_length:
                line=line[:i+1]+line[i+1].upper()+line[i+2:]  # 空格后首字母大写
            elif line[i]!=' ' and i+1<line_length:
                line=line[:i+1]+line[i+1].lower()+line[i+2:]  # 其他字母小写
        print(line)  # 输出格式化后的文本

if __name__=="__main__":
    main()