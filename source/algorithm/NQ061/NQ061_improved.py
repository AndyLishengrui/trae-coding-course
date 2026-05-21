import sys

def main():
    for line in sys.stdin:
        coords = list(map(float, line.strip().split()))
        rect1 = coords[:4]
        rect2 = coords[4:]
        
        # 确保每个矩形的x1 < x2, y1 < y2
        if rect1[0] > rect1[2]:
            rect1[0], rect1[2] = rect1[2], rect1[0]
        if rect1[1] > rect1[3]:
            rect1[1], rect1[3] = rect1[3], rect1[1]
        if rect2[0] > rect2[2]:
            rect2[0], rect2[2] = rect2[2], rect2[0]
        if rect2[1] > rect2[3]:
            rect2[1], rect2[3] = rect2[3], rect2[1]
        
        # 计算重叠区域的边界
        min_x = max(rect1[0], rect2[0])
        max_x = min(rect1[2], rect2[2])
        min_y = max(rect1[1], rect2[1])
        max_y = min(rect1[3], rect2[3])
        
        # 判断是否有重叠
        if min_x >= max_x or min_y >= max_y:
            print("0.00")
        else:
            area = (max_x - min_x) * (max_y - min_y)
            print("%.2f" % area)

if __name__ == "__main__":
    main()