def can_place(stalls, distance, C):
    count = 1
    last = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last >= distance:
            count += 1
            last = stalls[i]
            if count >= C:
                return True
    return False

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    C = int(input[idx])
    idx += 1
    stalls = []
    for _ in range(N):
        stalls.append(int(input[idx]))
        idx += 1
    stalls.sort()
    
    left = 1
    right = stalls[-1] - stalls[0]
    while left < right:
        mid = left + (right - left + 1) // 2
        if can_place(stalls, mid, C):
            left = mid
        else:
            right = mid - 1
    print(left)

if __name__ == "__main__":
    main()
