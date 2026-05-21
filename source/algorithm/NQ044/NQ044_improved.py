import sys

def check_password(s):
    length = len(s)
    if length < 8 or length > 16:
        return "NO"
    
    type_present = [0] * 4  # 0:小写, 1:大写, 2:数字, 3:特殊符号
    valid = True
    
    for ch in s:
        if ch.islower():
            type_present[0] = 1
        elif ch.isupper():
            type_present[1] = 1
        elif ch.isdigit():
            type_present[2] = 1
        elif ch in '~!@#$%^':
            type_present[3] = 1
        else:
            valid = False
            break
    
    if not valid:
        return "NO"
    
    return "YES" if sum(type_present) >= 3 else "NO"

def main():
    input = sys.stdin.read().split()
    t = int(input[0])
    
    for password in input[1:t+1]:
        print(check_password(password))

if __name__ == "__main__":
    main()