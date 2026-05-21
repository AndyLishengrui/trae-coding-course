def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    
    m = int(input[idx])
    idx += 1
    n = int(input[idx])
    idx += 1
    
    if m <= 0 or n <= 0:
        return
    
    scores = []
    for _ in range(m):
        row = list(map(int, input[idx:idx+n]))
        scores.append(row)
        idx += n
    
    max_row, max_col = 1, 1
    max_abs_score = abs(scores[0][0])
    
    for i in range(m):
        for j in range(n):
            current_abs = abs(scores[i][j])
            if current_abs > max_abs_score:
                max_abs_score = current_abs
                max_row, max_col = i + 1, j + 1
    
    print(max_row, max_col, scores[max_row-1][max_col-1])

if __name__ == "__main__":
    main()