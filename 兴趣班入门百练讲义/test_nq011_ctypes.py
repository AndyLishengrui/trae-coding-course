from ctypes import c_float
import math

def calculate_ctypes(n, m):
    res = c_float(0.0)
    a = c_float(n)
    for k in range(m):
        if a.value == 1.0:
            res.value += (m - k)
            break
        res.value += a.value
        # In C++, sqrt(float) returns float (overload). 
        # Python math.sqrt returns double.
        # We cast back to float by assigning to c_float field
        a.value = math.sqrt(a.value) 
    return res.value

inputs = [
    (65004, 5750),
    (87184, 2112),
    (94597, 561),
    (80010, 2732),
    (58744, 7710)
]

print("Python simulated float32 results:")
for n, m in inputs:
    val = calculate_ctypes(n, m)
    print(f"{n} {m} -> {val:.2f}")
