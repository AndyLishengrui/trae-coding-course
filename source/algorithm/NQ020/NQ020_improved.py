import sys

def main():
    try:
        input = sys.stdin.read
        data = input().split()
        if not data: return
        
        iterator = iter(data)
        t_str = next(iterator, None)
        if not t_str: return
        t = int(t_str)
        
        for _ in range(t):
            h = int(next(iterator))
            m = int(next(iterator))
            s = int(next(iterator))
            
            # 分针角度：每分钟6度
            m_ang = (m + s / 60.0) * 6.0
            
            # 时针角度：每小时30度
            h_ang = (h % 12 + (m + s / 60.0) / 60.0) * 30.0
            
            diff = abs(h_ang - m_ang)
            if diff > 180:
                diff = 360 - diff
                
            print(int(diff))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
