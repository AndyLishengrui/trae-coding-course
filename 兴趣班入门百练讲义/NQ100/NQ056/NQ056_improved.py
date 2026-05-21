import sys

# 判断三个数是否能构成三角形
def can_form_triangle(a, b, c):
    # 三角形的构成条件是任意两边之和大于第三边
    return (a + b > c) and (a + c > b) and (b + c > a)

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    
    for _ in range(n):
        a = int(input[ptr])
        b = int(input[ptr+1])
        c = int(input[ptr+2])
        ptr += 3
        
        if can_form_triangle(a, b, c):
            print("OK")
        else:
            print("NO")

if __name__ == "__main__":
    main()