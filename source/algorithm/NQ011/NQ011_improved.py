import math
import sys
from ctypes import c_float

def main():
    data = sys.stdin.read().split()
    iterator = iter(data)
    try:
        while True:
            n = next(iterator)
            m = next(iterator)
            
            n = int(float(n))
            m = int(float(m))
            
            res = c_float(0.0)
            a = c_float(n)
            for k in range(m):
                # Optimization: Square root converges to 1.0 very quickly.
                # Once it reaches 1.0, all subsequent terms are 1.0.
                if a.value == 1.0:
                    res.value += (m - k)
                    break
                
                res.value += a.value
                a.value = math.sqrt(a.value)
            print("%.2f" % res.value)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()