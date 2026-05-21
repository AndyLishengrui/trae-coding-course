# 初始数独盘面
initial_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_valid(grid):
    # 检查每一行
    for row in grid:
        used = set()
        for num in row:
            if num < 1 or num > 9 or num in used:
                return False
            used.add(num)
    
    # 检查每一列
    for col in range(9):
        used = set()
        for row in range(9):
            num = grid[row][col]
            if num in used:
                return False
            used.add(num)
    
    # 检查每一个3x3的小九宫格
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            used = set()
            for i in range(3):
                for j in range(3):
                    num = grid[br + i][bc + j]
                    if num in used:
                        return False
                    used.add(num)
    
    return True

def check_initial(grid):
    for i in range(9):
        for j in range(9):
            if initial_grid[i][j] != 0 and initial_grid[i][j] != grid[i][j]:
                return False
    return True

def read_grid():
    grid = []
    
    for i in range(9):
        line = input().strip()
        if len(line) != 9:
            return False
        
        row = []
        for c in line:
            if not c.isdigit() or int(c) < 1 or int(c) > 9:
                return False
            row.append(int(c))
        grid.append(row)
    
    return check_initial(grid) and is_valid(grid)

def main():
    print("Yes" if read_grid() else "No")

if __name__ == "__main__":
    main()